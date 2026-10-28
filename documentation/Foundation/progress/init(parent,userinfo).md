# init(parent:userInfo:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new progress instance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(parent parentProgressOrNil: Progress?, userInfo userInfoOrNil: [ProgressUserInfoKey : Any]? = nil)
```

```objc
- (instancetype) initWithParent:(NSProgress *) parentProgressOrNil userInfo:(NSDictionary<NSString *,id> *) userInfoOrNil;
```

## Discussion

This is the designated initializer for the [`Progress`](../progress.md) class.

## Parameters

- `parentProgressOrNil`: The containing [`Progress`](../progress.md) object, if any, to notify when reporting progress, or to consult when checking for cancellation.

  The only valid values are [`current()`](./current%28%29.md) or `nil`.
- `userInfoOrNil`: The optional user information dictionary for the progress object.

## See Also

### Creating Progress Objects
- [class func discreteProgress(totalUnitCount: Int64) -> Progress](./discreteprogress%28totalunitcount%29.md)
  Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.
- [init(totalUnitCount: Int64)](./init%28totalunitcount%29.md)
  Creates and returns a progress instance.
- [init(totalUnitCount: Int64, parent: Progress, pendingUnitCount: Int64)](./init%28totalunitcount,parent,pendingunitcount%29.md)
  Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/init(parent:userinfo:))*