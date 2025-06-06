# keyPathsAndRelativeValues(forViewerOffset:)

**Framework**: UIKit  
**Kind**: method

For a given set of offset values, returns the view properties (and corresponding values) to update.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func keyPathsAndRelativeValues(forViewerOffset viewerOffset: UIOffset) -> [String : Any]?
```

#### Return Value

A dictionary containing one or more key path strings representing the properties of the view to modify. The value associated with each key path string is the value to add to the given property—that is, it is the amount by which to change the current value of the property. Specify each key path relative to the view containing the motion effect object.

#### Discussion

Subclasses must override this method and use it to return the values to apply to a view when the user changes the relative orientation of the device’s screen. iOS computes the viewer offset values and calls this method so that subclassers can decide how that offset affects the underlying views. For example, you might use this method to modify the position of the view and its layer to give the view some visual depth.

```objc
NSDictionary* dict = @{
                         @"center" : [NSValue valueWithCGPoint:CGPointMake(3.4, 1.2)],                           @"layer.shadowOffset.width" : @(-1.1)
                      };
```

The key paths you return in the dictionary must refer to animatable properties. The motion effect object uses the returned information to animate the view’s properties to the new values. You can animate properties of the view, its layer, or any subviews that are accessible from the view’s properties.

## Parameters

- `viewerOffset`: The direction that the device is facing relative to the viewer. The range of each offset value is   to  . When the device’s screen is pointed directly at the user, the offset values are (0, 0). Rotating the phone so that the screen points down or to the right of the viewer yields a positive value. Rotating the phone so that the screen points above the user or to the user’s left yields a negative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimotioneffect/keypathsandrelativevalues(forvieweroffset:))*