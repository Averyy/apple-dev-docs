# transferRepresentation

**Framework**: Group Activities  
**Kind**: property  
**Role**: Type Property

A default type that lets the system share your activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var transferRepresentation: some TransferRepresentation { get }
```

Available when `Self` conforms to `Transferable`.

## Discussion

This property contains a default [`GroupActivityTransferRepresentation`](../groupactivitytransferrepresentation.md) for your activity. The system uses this type to offer your activity via SharePlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivity/transferrepresentation)*