# preferredName(for:basedOn:)

**Framework**: Swift Testing  
**Kind**: method  
**Required**: Yes

Generate a preferred name for the given attachment.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
borrowing func preferredName(for attachment: borrowing Attachment<Self>, basedOn suggestedName: String) -> String
```

#### Return Value

The preferred name for `attachment`.

#### Discussion

The testing library uses this function to determine the best name to use when saving `attachment`. The default implementation of this function returns `suggestedName` without any changes.

## Parameters

- `attachment`: The attachment that needs to be named.
- `suggestedName`: A suggested name to use as the basis of the preferred name. This string was provided by the developer when they initialized `attachment`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachable/preferredname(for:basedon:))*