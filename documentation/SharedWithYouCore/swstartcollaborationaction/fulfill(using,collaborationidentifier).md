# fulfill(using:collaborationIdentifier:)

**Framework**: SharedWithYouCore  
**Kind**: method  
**Role**: Instance Method

Informs an app to set up the universal link and device independent identifier to provide to the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func fulfill(using url: URL, collaborationIdentifier: SWCollaborationIdentifier)
```

```objc
- (void) fulfillUsingURL:(NSURL *) url collaborationIdentifier:(SWCollaborationIdentifier) collaborationIdentifier;
```

## Parameters

- `url`: The universal link to give to the system.
- `collaborationIdentifier`: The [`SWCollaborationIdentifier`](../swcollaborationidentifier.md) to give to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swstartcollaborationaction/fulfill(using:collaborationidentifier:))*