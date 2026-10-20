# PKPayLaterViewDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

Methods the framework calls when the Apple Pay Later view’s size changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```swift
protocol PKPayLaterViewDelegate : NSObjectProtocol
```

```objc
@protocol PKPayLaterViewDelegate <NSObject>
```

#### Overview

When manually laying out this view, adopt this protocol to receive a callback when the Apple Pay Layer view’s size changes.

## Topics

### Responding to view size changes
- [func payLaterViewDidUpdateHeight(PKPayLaterView)](./pkpaylaterviewdelegate/paylaterviewdidupdateheight%28_%29.md)
  Tells the delegate when the Apple Pay Later visual merchandising widget’s height changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to changes in the view’s height
- [var delegate: any PKPayLaterViewDelegate](./pkpaylaterview/delegate.md)
  A delegate object that receives messages about the changes to the Apple Pay Later view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterviewdelegate)*