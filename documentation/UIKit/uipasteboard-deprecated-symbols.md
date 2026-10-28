# Deprecated symbols

**Framework**: UIKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated
- [var isPersistent: Bool](./uipasteboard/ispersistent.md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func setPersistent(Bool)](./uipasteboard/setpersistent%28_%29.md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<Set<UIPasteboard.DetectionPattern>, any Error>) -> ())](./uipasteboard/detectpatterns%28for,completionhandler%29-5zlnd.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[Set<UIPasteboard.DetectionPattern>], any Error>) -> ())](./uipasteboard/detectpatterns%28for,initemset,completionhandler%29-29iwn.md)
  Determines whether pasteboard items match the specified patterns, without notifying the user.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<[UIPasteboard.DetectionPattern : Any], any Error>) -> ())](./uipasteboard/detectvalues%28for,completionhandler%29-9p2ff.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[[UIPasteboard.DetectionPattern : Any]], any Error>) -> ())](./uipasteboard/detectvalues%28for,initemset,completionhandler%29-8y0iw.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.

## See Also

### Deprecated
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](./uipasteboard/detectpatterns%28for,completionhandler%29-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())](./uipasteboard/detectpatterns%28for,initemset,completionhandler%29-7ubl1.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<UIPasteboard.DetectedValues, any Error>) -> ())](./uipasteboard/detectvalues%28for,completionhandler%29-6adre.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard-deprecated-symbols)*