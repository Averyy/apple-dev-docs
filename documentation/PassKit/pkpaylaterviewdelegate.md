# PKPayLaterViewDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol

Methods the framework calls when the Apple Pay Later view’s size changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol PKPayLaterViewDelegate : NSObjectProtocol
```

#### Overview

When manually laying out this view, adopt this protocol to receive a callback when the Apple Pay Layer view’s size changes.

## Topics

### Responding to view size changes
- [func payLaterViewDidUpdateHeight(PKPayLaterView)](pkpaylaterviewdelegate/paylaterviewdidupdateheight(_:).md)
  Tells the delegate when the Apple Pay Later visual merchandising widget’s height changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: any PKPayLaterViewDelegate](pkpaylaterview/delegate.md)
  A delegate object that receives messages about the changes to the Apple Pay Later view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterviewdelegate)*