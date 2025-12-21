# interfaceParametersDescription()

**Framework**: Foundation  
**Kind**: method

Returns a human-readable string describing the data that SiriKit displays to the user when you handle an intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func interfaceParametersDescription() -> String
```

#### Discussion

If you provide an Intents UI app extension, you can customize all or some of the interface that SiriKit displays to the user for a given intent. The information displayed by SiriKit is different for each intent, and can change in the future. During development, use this method to retrieve a human-readable description of the contents of the [`INParameter`](https://developer.apple.com/documentation/Intents/INParameter) objects that SiriKit intends to display for the current intent. Use that information to plan your custom interface.

For information about customizing the Siri and Maps interfaces, see [`Creating an Intents App Extension`](https://developer.apple.com/documentation/SiriKit/creating-an-intents-app-extension).

## See Also

- [var hostedViewMinimumAllowedSize: CGSize](nsextensioncontext/hostedviewminimumallowedsize.md)
  The minimum size for a Siri hosted view.
- [var hostedViewMaximumAllowedSize: CGSize](nsextensioncontext/hostedviewmaximumallowedsize.md)
  The maximum size for a Siri hosted view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/interfaceparametersdescription())*