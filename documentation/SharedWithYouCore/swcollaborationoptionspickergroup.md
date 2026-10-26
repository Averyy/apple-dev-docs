# SWCollaborationOptionsPickerGroup

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that represents a group of collaboration options that the system displays together with mutually exclusive options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationOptionsPickerGroup
```

```objc
@interface SWCollaborationOptionsPickerGroup : SWCollaborationOptionsGroup
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

#### Overview

`SWCollaborationOptionsPickerGroup` displays as a picker view. A person can select only one option in the group. To allow a person to select more than one option, use [`SWCollaborationOptionsGroup`](./swcollaborationoptionsgroup.md).

## Topics

### Accessing options group attributes
- [var selectedOptionIdentifier: String](./swcollaborationoptionspickergroup/selectedoptionidentifier.md)
  The identifier of the selected option in the group.

## Relationships

### Inherits From
- [SWCollaborationOptionsGroup](./swcollaborationoptionsgroup.md)
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
- [class SWCollaborationShareOptions](./swcollaborationshareoptions.md)
  An object that represents the state of the collaboration options for the document.
- [struct SWLocalCollaborationIdentifier](./swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let UTCollaborationOptionsTypeIdentifier: String](./utcollaborationoptionstypeidentifier.md)
  A string constant for the options type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoptionspickergroup)*