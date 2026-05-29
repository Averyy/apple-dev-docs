# filter

**Framework**: Core Animation  
**Kind**: property

An optional Core Image filter object that provides the transition.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var filter: Any? { get set }
```

#### Discussion

If specified, the filter must support both [`kCIInputImageKey`](https://developer.apple.com/documentation/CoreImage/kCIInputImageKey) and [`kCIInputTargetImageKey`](https://developer.apple.com/documentation/CoreImage/kCIInputTargetImageKey) input keys, and the [`kCIOutputImageKey`](https://developer.apple.com/documentation/CoreImage/kCIOutputImageKey) output key.  The filter may optionally support the [`kCIInputExtentKey`](https://developer.apple.com/documentation/CoreImage/kCIInputExtentKey) input key, which is set to a rectangle describing the region in which the transition should run. If `filter` does not support the required input and output keys the behavior is undefined.

Defaults to `nil`. When a transition filter is specified the [`type`](catransition/type.md) and [`subtype`](catransition/subtype.md) properties are ignored.

The [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) that contains the transitioning layer must have its [`layerUsesCoreImageFilters`](https://developer.apple.com/documentation/AppKit/NSView/layerUsesCoreImageFilters) set to [`true`](https://developer.apple.com/documentation/Swift/true).

The following code shows how you can transition between the two states of a [`CATextLayer`](catextlayer.md) named `transitioningLayer`. When the layer is first created, its [`backgroundColor`](calayer/backgroundcolor.md) is set to red and its [`string`](catextlayer/string.md) property is set to `Red`. When the `runTransition()` function is called, a new [`CATransition`](catransition.md) object is created and added to `transitioningLayer`, and the state of the layer is changed so that its background color is blue and its rendered text reads `Blue`.

The end result is that the transition animates from the red state to the blue state using a [`CICopyMachineTransition`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CICopyMachineTransition) transition.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    view.layerUsesCoreImageFilters = true
    
    view.layer = CALayer()
    
    transitioningLayer.frame = CGRect(x: 10, y: 10,
                                      width: 320, height: 160)
    
    view.layer!.addSublayer(transitioningLayer)
    
    // Initial "red" state
    transitioningLayer.backgroundColor = NSColor.red.cgColor
    transitioningLayer.string = "Red"
}
     
func runTransition() {
    let transition = CATransition()
    transition.duration = 2
    
    transition.filter = CIFilter(name: "CICopyMachineTransition")
    transitioningLayer.add(transition,
                           forKey: "transition")
    
    // Transition to "blue" state
    transitioningLayer.backgroundColor = NSColor.blue.cgColor
    transitioningLayer.string = "Blue"
}
```

##### Special Considerations

This property is not supported on layers in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransition/filter)*