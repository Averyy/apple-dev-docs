# insertCollaborationItemProvider(_:completionHandler:)

**Framework**: Message UI  
**Kind**: method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func insertCollaborationItemProvider(_ itemProvider: NSItemProvider) async -> Bool
```

#### Discussion

If the return value is YES, the itemProvider was added to the composition.  The itemProvider must be non-nil.

## Parameters

- `itemProvider`: Specifying the intended content for collaboration


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/insertcollaborationitemprovider(_:completionhandler:))*