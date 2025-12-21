# filters

**Framework**: SceneKit  
**Kind**: property

An array of Core Image filters to be applied to the rendered contents of the node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var filters: [CIFilter]? { get set }
```

#### Discussion

An array of [`CIFilter`](https://developer.apple.com/documentation/CoreImage/CIFilter-swift.class) objects.

When this array is nonempty, SceneKit renders the node (and its child node hierarchy) into an image buffer and then applies the filters before compositing the filters’ output into the rendered scene. The order of the array determines the order of the Core Image filter chain. For example, the following code applies a pixellate filter to the rendered node and then a blur filter to the output of the pixellate filter:

```swift
let gaussianBlurFilter = CIFilter(name: "CIGaussianBlur")
gaussianBlurFilter.name = "blur"
let pixellateFilter = CIFilter(name: CIPixellate")
node.filters = [ pixellateFilter, gaussianBlurFilter ]
```

```objc
CIFilter *gaussianBlurFilter = [CIFilter filterWithName:@"CIGaussianBlur"];
gaussianBlurFilter.name = @"blur";
CIFilter *pixellateFilter = [CIFilter filterWithName:@"CIPixellate"];
pixellateFilter.name = @"pixellate";
node.filters = @[ pixellateFilter, gaussianBlurFilter ];
```

After you attach filters to a node, you can modify filter parameters only by calling [`setValue(_:forKeyPath:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forKeyPath:)) on the node the filter is attached to. (Directly modifying the parameters of a filter attached to a node results in undefined behavior.) To refer to a filter by key path, you must set the filter’s `name` property to a string that uniquely identifies that filter instance, as shown in the code above.

You can also animate filter parameters by their key paths, as in the code below that animates one of the filters from the previous example.

```swift
let animation = CABasicAnimation(keyPath: "filters.pixellate.inputScale") // user name set on filter instance above
animation.toValue = 50
animation.fromValue = 0
animation.autoreverses = true
animation.repeatCount = .infinity
animation.duration = 2.0
node.add(animation, forKey: nil)
```

```objc
CAAnimation *animation = [CABasicAnimation animationWithKeyPath:@"filters.pixellate.inputScale"]; // use name set on filter instance above
animation.toValue = @50;
animation.fromValue = @0;
animation.autoreverses = YES;
animation.repeatCount = FLT_MAX;
animation.duration = 2.0;
[node addAnimation:animation forKey:nil];
```

## See Also

- [var rendererDelegate: (any SCNNodeRendererDelegate)?](scnnode/rendererdelegate.md)
  An object responsible for rendering custom contents for the node using Metal or OpenGL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/filters)*