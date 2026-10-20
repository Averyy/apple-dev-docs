# enumerateIndexPaths(options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.11+

## Declaration

```swift
func enumerateIndexPaths(options opts: NSEnumerationOptions = [], using block: (IndexPath, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateIndexPathsWithOptions:(NSEnumerationOptions) opts usingBlock:(void (^)(NSIndexPath *indexPath, BOOL *stop)) block;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/enumerateindexpaths(options:using:))*