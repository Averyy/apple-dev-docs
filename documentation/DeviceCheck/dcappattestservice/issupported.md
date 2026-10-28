# isSupported

**Framework**: DeviceCheck  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a particular device provides the App Attest service.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isSupported: Bool { get }
```

```objc
@property (readonly, getter=isSupported) BOOL supported;
```

## Mentions

- [Establishing your app’s integrity](../establishing-your-app-s-integrity.md)

## Discussion

> ❗ **Important**: Not all device types support the App Attest service, so check for support before using the service.
>
> If you read [`isSupported`](./issupported.md) from an app running on a Mac device, the value is [`false`](../../Swift/false.md). This includes Mac Catalyst apps, and iOS or iPadOS apps running on Apple silicon.

If you read [`isSupported`](./issupported.md) from within an app extension, the value might be [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md), depending on the extension type. However, most extensions don’t support App Attest. The [`generateKey(completionHandler:)`](./generatekey%28completionhandler%29.md) method fails when you call it from an app extension, regardless of the value of [`isSupported`](./issupported.md).

The only app extensions that support App Attest are watchOS extensions in watchOS 9 or later. For these extensions, you can use the results from [`isSupported`](./issupported.md) to indicate whether your WatchKit extension bypasses attestation.

## See Also

### Accessing the service
- [class var shared: DCAppAttestService](./shared.md)
  The shared App Attest service that you use to validate your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcappattestservice/issupported)*