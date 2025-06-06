# edited(_:range:changeInLength:)

**Framework**: UIKit  
**Kind**: method

Tracks changes made to the text storage object, allowing the text storage to record the full extent of changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func edited(_ editedMask: NSTextStorage.EditActions, range editedRange: NSRange, changeInLength delta: Int)
```

#### Discussion

This method invokes [`processEditing()`](nstextstorage/processediting().md) if there are no outstanding [`beginEditing()`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1411853-beginediting) calls. `NSTextStorage` invokes this method automatically each time it makes a change to its attributed string. Subclasses that override or add methods that alter their attributed strings directly should invoke this method after making those changes; otherwise you shouldn’t invoke this method. The information accumulated with this method is then used in an invocation of [`processEditing()`](nstextstorage/processediting().md) to report the affected portion of the receiver.

The methods for querying changes, [`editedRange`](nstextstorage/editedrange.md) and [`changeInLength`](nstextstorage/changeinlength.md), indicate the extent of characters affected after the change. This method expects the characters before the change because that information is readily available as the argument to whatever method performs the change (such as [`replaceCharacters(in:with:)`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1418451-replacecharacters)).

## Parameters

- `editedMask`: A mask specifying the nature of the changes. You make the value by combining with the C bitwise OR operator the options described in  .
- `editedRange`: The extent of characters affected before the change took place.
- `delta`: The number of characters added to or removed from  . If no characters where edited as noted by  , its value is irrelevant and undefined. For example, when replacing “The” with “Several” in the string “The files couldn’t be saved”,   is {0, 3} and   is 4.

## See Also

- [func processEditing()](nstextstorage/processediting.md)
  Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/edited(_:range:changeinlength:))*