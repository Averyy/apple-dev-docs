# SWCollaborationOption

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that determines how the system shares a document in a collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationOption
```

```objc
@interface SWCollaborationOption : NSObject
```

#### Overview

The `SWCollaborationOption` represents a user-configurable setting for a collaboration that the system uses to share the document. The system displays these options on the Share Sheet or in Messages.

## Topics

### Creating collaboration options
- [init(title: String, identifier: String)](./swcollaborationoption/init%28title,identifier%29.md)
  Creates and initializes a collaboration option object with a provided title and identifier.
- [convenience init(title: String, identifier: String, subtitle: String, selected: Bool, requiredOptionsIdentifiers: [String])](./swcollaborationoption/init%28title,identifier,subtitle,selected,requiredoptionsidentifiers%29.md)
  Creates and initializes a collaboration option object with the provided values.
### Accessing option attributes
- [var identifier: String](./swcollaborationoption/identifier.md)
  A unique identifier.
- [var isSelected: Bool](./swcollaborationoption/isselected.md)
  A Boolean value that represents the selected state of an option.
- [var requiredOptionsIdentifiers: [String]](./swcollaborationoption/requiredoptionsidentifiers.md)
  An array of option identifiers that the app must select before the system makes the option interactive.
- [var subtitle: String](./swcollaborationoption/subtitle.md)
  A localized string the system displays to represent the permissions option in the collaboration view.
- [var title: String](./swcollaborationoption/title.md)
  A localized string the system displays as a title to represent the permissions option.
### Initializers
- [init?(coder: NSCoder)](./swcollaborationoption/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Manage options in a collaboration
- [class SWCollaborationOptionsGroup](./swcollaborationoptionsgroup.md)
  An object that represents a group of collaboration options that the system displays together.
- [class SWCollaborationOptionsPickerGroup](./swcollaborationoptionspickergroup.md)
  An object that represents a group of collaboration options that the system displays together with mutually exclusive options.
- [class SWCollaborationShareOptions](./swcollaborationshareoptions.md)
  An object that represents the state of the collaboration options for the document.
- [struct SWLocalCollaborationIdentifier](./swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let UTCollaborationOptionsTypeIdentifier: String](./utcollaborationoptionstypeidentifier.md)
  A string constant for the options type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoption)*