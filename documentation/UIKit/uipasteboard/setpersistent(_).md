# setPersistent(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates whether the pasteboard is persistent.

**Availability**:
- iOS 3.0+ - Deprecated in 10.0
- iPadOS 3.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use shared app group containers instead. For more information about app groups, see [Adding an App to an App Group](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW19). For more information about shared containers, see the [`containerURL(forSecurityApplicationGroupIdentifier:)`](../../Foundation/filemanager/containerurl%28forsecurityapplicationgroupidentifier%29.md) method of [`FileManager`](../../Foundation/filemanager.md).

## Declaration

```swift
func setPersistent(_ persistent: Bool)
```

```objc
- (void) setPersistent:(BOOL) persistent;
```

#### Discussion

Nonpersistent named pasteboards remain available. You can use these to implement such features as Duplicate or Copy Style. A nonpersistent named pasteboard is available only in the process that creates it.

## See Also

### Deprecated
- [var isPersistent: Bool](./ispersistent.md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<Set<UIPasteboard.DetectionPattern>, any Error>) -> ())](./detectpatterns%28for,completionhandler%29-5zlnd.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[Set<UIPasteboard.DetectionPattern>], any Error>) -> ())](./detectpatterns%28for,initemset,completionhandler%29-29iwn.md)
  Determines whether pasteboard items match the specified patterns, without notifying the user.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<[UIPasteboard.DetectionPattern : Any], any Error>) -> ())](./detectvalues%28for,completionhandler%29-9p2ff.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[[UIPasteboard.DetectionPattern : Any]], any Error>) -> ())](./detectvalues%28for,initemset,completionhandler%29-8y0iw.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setpersistent(_:))*