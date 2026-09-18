# CPPanel

**Framework**: CarPlay  
**Kind**: class

A type that provides the common behaviors for panels you display on top of your app’s content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPPanel
```

#### Overview

The `CPPanel` type defines the default behaviors for panels you display in your app. You don’t create or present this type directly. Instead, instantiate one of the defined subclasses and present that type from your app’s interface. For example, create a [`CPMapPanel`](cpmappanel.md) and configure it with navigation-related data, and present it from a [`CPMapTemplate`](cpmaptemplate.md) to overlay that information on top of your custom map.

## Topics

### Initializers
- [init?(coder: NSCoder)](cppanel/init(coder:).md)
### Instance Properties
- [var showsCloseButton: Bool](cppanel/showsclosebutton.md)
  A Boolean value that indicates whether the panel displays a close button.
### Type Properties
- [class var maximumPanelItemsCount: Int](cppanel/maximumpanelitemscount.md)
  The maximum number of items the panel is able to display.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CPMapPanel](cpmappanel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanel)*