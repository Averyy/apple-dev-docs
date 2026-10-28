# detectValuesForPatterns:completionHandler:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```objc
- (void) detectValuesForPatterns:(NSSet<NSString *> *) patterns completionHandler:(void (^)(NSDictionary<NSString *,id> *, NSError *)) completionHandler;
```

## Discussion

> ❗ **Important**:  Calling this method notifies the user that the app has read the contents of the pasteboard.

For details about the types returned for each pattern, see [`UIPasteboard.DetectionPattern`](./detectionpattern.md).

## Parameters

- `patterns`: The patterns to detect on the pasteboard.
- `completionHandler`: A block that the system invokes after detecting patterns on the pasteboard. The block takes a `Result` parameter that contains either a dictionary with the patterns found on the pasteboard or an error if detection failed. If the `Result` instance contains a dictionary, the keys specify the matched pattern, and the value specifies the content of the pasteboard.

## See Also

### Detecting patterns of content in pasteboard items
- [- detectPatternsForPatterns:completionHandler:](./detectpatternsforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [- detectPatternsForPatterns:inItemSet:completionHandler:](./detectpatternsforpatterns_initemset_completionhandler_.md)
  Determines whether pasteboard items match the specified patterns, without notifying the user.
- [- detectValuesForPatterns:inItemSet:completionHandler:](./detectvaluesforpatterns_initemset_completionhandler_.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.
- [UIPasteboard.DetectionPattern](./detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectvaluesforpatterns:completionhandler:)*