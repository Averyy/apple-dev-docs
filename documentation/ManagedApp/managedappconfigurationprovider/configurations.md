# configurations(_:)

**Framework**: ManagedApp  
**Kind**: method

Provides an asynchronous sequence of configurations that the MDM admin specifies.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func configurations<Configuration>(_ t: Configuration.Type) async -> some AsyncSequence<Optional<Configuration>, Never> where Configuration : Decodable
```

## Mentions

- [Specifying and decoding a configuration](specifying-and-decoding-a-configuration.md)

#### Return Value

An [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) of optionals of the specified type. When the framework instantiates the result, the sequence yields the current configuration immediately. The sequence yields `nil` if a decoding error occurs or if the MDM admin currently provides no configuration for the app.

#### Discussion

The MDM server provides an encoded configuration to the framework using [`Device Management`](https://developer.apple.com/documentation/DeviceManagement). The argument you pass in to this method is a type you implement that decodes the configuration definition. Your custom type also becomes the element of the returned sequence. Your decoder processes the configuration according to your specification, which the MDM admin uses to define the configuration on the server.

When you begin iterating the returned sequence using `for await`, the sequence yields the current configuration immediately, or `nil` if the MDM admin hasn’t provided a configuration. If the MDM admin provides or changes the configuration at runtime, the sequence yields a new configuration object if decoding succeeds. If decoding fails, the framework discards the updated configuration and the sequence yields `nil`.

In addition, the type you pass in can:

- Use default values for optional portions of the configuration not provided by the MDM server.
- Validate expected ranges for values.
- Perform other custom validation.

The device reports the result of decoding to the MDM server. On success, the device reports a valid state to the server. However, if the decoder throws an error conforming to [`ManagedAppConfigurationDecodingError`](managedappconfigurationdecodingerror.md), the device reports an invalid state to the server and logs an error that contains the [`code`](managedappconfigurationdecodingerror/code.md) and [`message`](managedappconfigurationdecodingerror/message.md) properties. The MDM admin can use the device’s event log to understand the cause when the server receives an invalid state.

If the decoder throws an error that doesn’t conform to [`ManagedAppConfigurationDecodingError`](managedappconfigurationdecodingerror.md) or if the error code is reserved, the device reports a generic error.

For more information on status reporting, see [`Leveraging the declarative management data model to scale devices`](https://developer.apple.com/documentation/DeviceManagement/leveraging-the-declarative-management-data-model-to-scale-devices#Use-status-to-report-device-state), and [`Status Reports`](https://developer.apple.com/documentation/DeviceManagement/status-reports).

## Parameters

- `t`: A type you provide that decodes and validates the configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappconfigurationprovider/configurations(_:))*