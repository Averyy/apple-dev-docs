# detectPatternsForPatterns:inItemSet:completionHandler:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether pasteboard items match the specified patterns, without notifying the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```objc
- (void) detectPatternsForPatterns:(NSSet<NSString *> *) patterns inItemSet:(NSIndexSet *) itemSet completionHandler:(void (^)(NSArray<NSSet<NSString *> *> *, NSError *)) completionHandler;
```

## Discussion

Because this method only detects for the presence of patterns and does not read the contents of the pasteboard, the system doesn’t notify the user about reading the contents of the pasteboard.

## Parameters

- `patterns`: The patterns to detect on the pasteboard.
- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass `nil` to detect patterns in all pasteboard items.
- `completionHandler`: A block that the system invokes after detecting patterns on the pasteboard. The block receives a `Result` instance that contains either an array with the patterns found on the pasteboard or an error if detection failed. If the `Result` instance contains an array, the index of each element in the array corresponds to the pasteboard item index specified in `itemSet`.

## See Also

### Detecting patterns of content in pasteboard items
- [- detectPatternsForPatterns:completionHandler:](./detectpatternsforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [- detectValuesForPatterns:completionHandler:](./detectvaluesforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [- detectValuesForPatterns:inItemSet:completionHandler:](./detectvaluesforpatterns_initemset_completionhandler_.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.
- [UIPasteboard.DetectionPattern](./detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectpatternsforpatterns:initemset:completionhandler:)*