# SWCollaborationShareOptions

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that represents the state of the collaboration options for the document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationShareOptions
```

```objc
@interface SWCollaborationShareOptions : NSObject
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Topics

### Creating share options
- [init(coder: NSCoder)](./swcollaborationshareoptions/init%28coder%29.md)
  Creates and initializes a collaboration share options object.
- [convenience init(optionsGroups: [SWCollaborationOptionsGroup])](./swcollaborationshareoptions/init%28optionsgroups%29.md)
  Creates and initializes a collaboration share options object with the array of groups.
- [init(optionsGroups: [SWCollaborationOptionsGroup], summary: String)](./swcollaborationshareoptions/init%28optionsgroups,summary%29.md)
  Creates and initializes a collaboration share options object the array of groups and a summary string.
### Accessing options attributes
- [var optionsGroups: [SWCollaborationOptionsGroup]](./swcollaborationshareoptions/optionsgroups.md)
  An array of options group objects to customize how the system shares the collaboration.
- [var summary: String](./swcollaborationshareoptions/summary.md)
  A localized string to summarize the collaboration options.

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
- [class SWCollaborationOption](./swcollaborationoption.md)
  An object that determines how the system shares a document in a collaboration.
- [class SWCollaborationOptionsGroup](./swcollaborationoptionsgroup.md)
  An object that represents a group of collaboration options that the system displays together.
- [class SWCollaborationOptionsPickerGroup](./swcollaborationoptionspickergroup.md)
  An object that represents a group of collaboration options that the system displays together with mutually exclusive options.
- [struct SWLocalCollaborationIdentifier](./swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let UTCollaborationOptionsTypeIdentifier: String](./utcollaborationoptionstypeidentifier.md)
  A string constant for the options type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationshareoptions)*