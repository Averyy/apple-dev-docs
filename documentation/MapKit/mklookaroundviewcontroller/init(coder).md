# init(coder:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a new LookAround view controller object from a coder object provided by a storyboard or nib file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The [`NSCoder`](../../Foundation/nscoder.md) object

## See Also

### Creating a LookAround controller
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Creates a new LookAround view controller from the specified nib and bundle.
- [init(scene: MKLookAroundScene)](./init%28scene%29.md)
  Creates a new LookAround view controller with the specified scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller/init(coder:))*