# CNBoundsPrediction

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object representing the bounds of the predicted subject.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNBoundsPrediction : NSObject
```

## Topics

### Instance Properties
- [confidence](./cnboundsprediction-c.class/confidence.md)
  A number between 0.0 and 1.0 representing the probability that a defined object is within the bounds.
- [normalizedBounds](./cnboundsprediction-c.class/normalizedbounds.md)
  The bounds of the detected object in normalized coordinates where (0.0, 0.0) is the upper-left corner, and (1.0, 1.0) is the lower-right.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)

## See Also

### Custom Object Tracking
- [CNObjectTracker](./cnobjecttracker-7aliq.md)
  An object that converts a normalized point or rectangle into a detection track that tracks an object over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnboundsprediction-c.class)*