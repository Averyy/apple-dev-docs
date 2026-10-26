# SWCollaborationOptionsGroup

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that represents a group of collaboration options that the system displays together.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationOptionsGroup
```

```objc
@interface SWCollaborationOptionsGroup : NSObject
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Topics

### Creating a collaboration options group
- [init(identifier: String, options: [SWCollaborationOption])](./swcollaborationoptionsgroup/init%28identifier,options%29.md)
  Creates and initializes a collaboration options group object.
### Accessing options group attributes
- [var footer: String](./swcollaborationoptionsgroup/footer.md)
  A localized string that provides additional information for the group of options.
- [var identifier: String](./swcollaborationoptionsgroup/identifier.md)
  A unique identifier.
- [var options: [SWCollaborationOption]](./swcollaborationoptionsgroup/options.md)
  An array of collaboration options the system displays as a group.
- [var title: String](./swcollaborationoptionsgroup/title.md)
  A localized string the system displays as the title of the group section.
### Initializers
- [init?(coder: NSCoder)](./swcollaborationoptionsgroup/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SWCollaborationOptionsPickerGroup](./swcollaborationoptionspickergroup.md)
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
- [class SWCollaborationOption](./swcollaborationoption.md)
  An object that determines how the system shares a document in a collaboration.
- [class SWCollaborationOptionsPickerGroup](./swcollaborationoptionspickergroup.md)
  An object that represents a group of collaboration options that the system displays together with mutually exclusive options.
- [class SWCollaborationShareOptions](./swcollaborationshareoptions.md)
  An object that represents the state of the collaboration options for the document.
- [struct SWLocalCollaborationIdentifier](./swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let UTCollaborationOptionsTypeIdentifier: String](./utcollaborationoptionstypeidentifier.md)
  A string constant for the options type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoptionsgroup)*