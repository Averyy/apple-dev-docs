# slideshowDidChangeCurrentIndex(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Performs custom tasks when the slideshow changes to the item at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func slideshowDidChangeCurrentIndex(_ newIndex: Int)
```

```objc
- (void) slideshowDidChangeCurrentIndex:(NSUInteger) newIndex;
```

#### Discussion

Image Kit invokes this method when the slideshow changes to the specified item. Implement this method to perform custom tasks at that time.

## Parameters

- `newIndex`: The index of the current item.

## See Also

### Performing Custom Tasks
- [func slideshowWillStart()](./slideshowwillstart%28%29.md)
  Performs custom tasks when the slideshow is about to start.
- [func slideshowDidStop()](./slideshowdidstop%28%29.md)
  Performs custom tasks when the slideshow stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/slideshowdidchangecurrentindex(_:))*