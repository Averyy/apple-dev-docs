# UIPasteConfiguration

**Framework**: UIKit  
**Kind**: class

The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPasteConfiguration
```

## Topics

### Initializing a paste configuration
- [init()](uipasteconfiguration/init.md)
  Initializes a new paste configuration.
- [convenience init(acceptableTypeIdentifiers: [String])](uipasteconfiguration/init(acceptabletypeidentifiers:).md)
  Initializes a new paste configuration with a specified array of acceptable UTIs.
- [convenience init(forAccepting: any NSItemProviderReading.Type)](uipasteconfiguration/init(foraccepting:)-6is3h.md)
  Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [convenience init<T>(forAccepting: T.Type)](uipasteconfiguration/init(foraccepting:)-84r2r.md)
### Getting acceptable type identifiers
- [var acceptableTypeIdentifiers: [String]](uipasteconfiguration/acceptabletypeidentifiers.md)
  An array of UTI strings that specify the types accepted by the paste configuration.
### Adding acceptable type identifiers
- [func addAcceptableTypeIdentifiers([String])](uipasteconfiguration/addacceptabletypeidentifiers(_:).md)
  Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.
- [func addTypeIdentifiers(forAccepting: any NSItemProviderReading.Type)](uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6.md)
  Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.
- [func addTypeIdentifiers<T>(forAccepting: T.Type)](uipasteconfiguration/addtypeidentifiers(foraccepting:)-8af7o.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPasteControl](uipastecontrol.md)
  A button that a person taps to place pasteboard contents in your app.
- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
- [class UIPasteboard](uipasteboard.md)
  An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration)*