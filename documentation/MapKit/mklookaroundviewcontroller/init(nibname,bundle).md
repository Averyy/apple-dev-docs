# init(nibName:bundle:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a new LookAround view controller from the specified nib and bundle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

```objc
- (instancetype) initWithNibName:(NSString *) nibNameOrNil bundle:(NSBundle *) nibBundleOrNil;
```

## Parameters

- `nibNameOrNil`: The name of the nib file.
- `nibBundleOrNil`: The [`Bundle`](../../Foundation/bundle.md) file.

## See Also

### Creating a LookAround controller
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new LookAround view controller object from a coder object provided by a storyboard or nib file.
- [init(scene: MKLookAroundScene)](./init%28scene%29.md)
  Creates a new LookAround view controller with the specified scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller/init(nibname:bundle:))*