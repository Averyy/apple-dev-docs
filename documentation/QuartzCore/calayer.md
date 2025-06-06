# CALayer

**Framework**: Core Animation  
**Kind**: class

An object that manages image-based content and allows you to perform animations on that content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CALayer
```

#### Overview

Layers are often used to provide the backing store for views but can also be used without a view to display content. A layer’s main job is to manage the visual content that you provide but the layer itself has visual attributes that can be set, such as a background color, border, and shadow. In addition to managing visual content, the layer also maintains information about the geometry of its content (such as its position, size, and transform) that is used to present that content onscreen. Modifying the properties of the layer is how you initiate animations on the layer’s content or geometry. A layer object encapsulates the duration and pacing of a layer and its animations by adopting the [`CAMediaTiming`](camediatiming.md) protocol, which defines the layer’s timing information.

If the layer object was created by a view, the view typically assigns itself as the layer’s delegate automatically, and you should not change that relationship. For layers you create yourself, you can assign a [`delegate`](calayer/delegate.md) object and use that object to provide the contents of the layer dynamically and perform other tasks. A layer may also have a layout manager object (assigned to the [`layoutManager`](calayer/layoutmanager.md) property) to manage the layout of subviews separately.

## Topics

### Creating a Layer
- [init()](calayer/init.md)
  Returns an initialized `CALayer` object.
- [init(layer: Any)](calayer/init(layer:).md)
  Override to copy or initialize custom fields of the specified layer.
- [init(remoteClientId: UInt32)](calayer/init(remoteclientid:).md)
  Initializes a layer with a remote client ID.
### Accessing Related Layer Objects
- [func presentation() -> Self?](calayer/presentation.md)
  Returns a copy of the presentation layer object that represents the state of the layer as it currently appears onscreen.
- [func model() -> Self](calayer/model.md)
  Returns the model layer object associated with the receiver, if any.
### Accessing the Delegate
- [var delegate: (any CALayerDelegate)?](calayer/delegate.md)
  The layer’s delegate object.
### Providing the Layer’s Content
- [var contents: Any?](calayer/contents.md)
  An object that provides the contents of the layer. Animatable.
- [var contentsRect: CGRect](calayer/contentsrect.md)
  The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [var contentsCenter: CGRect](calayer/contentscenter.md)
  The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [func display()](calayer/display.md)
  Reloads the content of this layer.
- [func draw(in: CGContext)](calayer/draw(in:).md)
  Draws the layer’s content using the specified graphics context.
### Modifying the Layer’s Appearance
- [var contentsGravity: CALayerContentsGravity](calayer/contentsgravity.md)
  A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](contents-gravity-values.md)
  The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [`contentsGravity`](calayer/contentsgravity.md) property.
- [var opacity: Float](calayer/opacity.md)
  The opacity of the receiver. Animatable.
- [var isHidden: Bool](calayer/ishidden.md)
  A Boolean indicating whether the layer is displayed. Animatable.
- [var masksToBounds: Bool](calayer/maskstobounds.md)
  A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [var mask: CALayer?](calayer/mask.md)
  An optional layer whose alpha channel is used to mask the layer’s content.
- [var isDoubleSided: Bool](calayer/isdoublesided.md)
  A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [var cornerRadius: CGFloat](calayer/cornerradius.md)
  The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [var maskedCorners: CACornerMask](calayer/maskedcorners.md)
- [struct CACornerMask](cacornermask.md)
- [var borderWidth: CGFloat](calayer/borderwidth.md)
  The width of the layer’s border. Animatable.
- [var borderColor: CGColor?](calayer/bordercolor.md)
  The color of the layer’s border. Animatable.
- [var backgroundColor: CGColor?](calayer/backgroundcolor.md)
  The background color of the receiver. Animatable.
- [var shadowOpacity: Float](calayer/shadowopacity.md)
  The opacity of the layer’s shadow. Animatable.
- [var shadowRadius: CGFloat](calayer/shadowradius.md)
  The blur radius (in points) used to render the layer’s shadow. Animatable.
- [var shadowOffset: CGSize](calayer/shadowoffset.md)
  The offset (in points) of the layer’s shadow. Animatable.
- [var shadowColor: CGColor?](calayer/shadowcolor.md)
  The color of the layer’s shadow. Animatable.
- [var shadowPath: CGPath?](calayer/shadowpath.md)
  The shape of the layer’s shadow. Animatable.
- [var style: [AnyHashable : Any]?](calayer/style.md)
  An optional dictionary used to store property values that aren’t explicitly defined by the layer.
- [var allowsEdgeAntialiasing: Bool](calayer/allowsedgeantialiasing.md)
  A Boolean indicating whether the layer is allowed to perform edge antialiasing.
- [var allowsGroupOpacity: Bool](calayer/allowsgroupopacity.md)
  A Boolean indicating whether the layer is allowed to composite itself as a group separate from its parent.
### Layer Filters
- [var filters: [Any]?](calayer/filters.md)
  An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [var compositingFilter: Any?](calayer/compositingfilter.md)
  A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [var backgroundFilters: [Any]?](calayer/backgroundfilters.md)
  An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [var minificationFilter: CALayerContentsFilter](calayer/minificationfilter.md)
  The filter used when reducing the size of the content.
- [var minificationFilterBias: Float](calayer/minificationfilterbias.md)
  The bias factor used by the minification filter to determine the levels of detail.
- [var magnificationFilter: CALayerContentsFilter](calayer/magnificationfilter.md)
  The filter used when increasing the size of the content.
### Configuring the Layer’s Rendering Behavior
- [var isOpaque: Bool](calayer/isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](calayer/edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
- [func contentsAreFlipped() -> Bool](calayer/contentsareflipped.md)
  Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [var isGeometryFlipped: Bool](calayer/isgeometryflipped.md)
  A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [var drawsAsynchronously: Bool](calayer/drawsasynchronously.md)
  A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [var shouldRasterize: Bool](calayer/shouldrasterize.md)
  A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [var rasterizationScale: CGFloat](calayer/rasterizationscale.md)
  The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [var contentsFormat: CALayerContentsFormat](calayer/contentsformat.md)
  A hint for the desired storage format of the layer contents.
- [func render(in: CGContext)](calayer/render(in:).md)
  Renders the layer and its sublayers into the specified context.
### Modifying the Layer Geometry
- [var frame: CGRect](calayer/frame.md)
  The layer’s frame rectangle.
- [var bounds: CGRect](calayer/bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var position: CGPoint](calayer/position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var zPosition: CGFloat](calayer/zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPointZ: CGFloat](calayer/anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var anchorPoint: CGPoint](calayer/anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [var contentsScale: CGFloat](calayer/contentsscale.md)
  The scale factor applied to the layer.
### Managing the Layer’s Transform
- [var transform: CATransform3D](calayer/transform.md)
  The transform applied to the layer’s contents. Animatable.
- [var sublayerTransform: CATransform3D](calayer/sublayertransform.md)
  Specifies the transform to apply to sublayers when rendering. Animatable.
- [func affineTransform() -> CGAffineTransform](calayer/affinetransform.md)
  Returns an affine version of the layer’s transform.
- [func setAffineTransform(CGAffineTransform)](calayer/setaffinetransform(_:).md)
  Sets the layer’s transform to the specified affine transform.
### Managing the Layer Hierarchy
- [var sublayers: [CALayer]?](calayer/sublayers.md)
  An array containing the layer’s sublayers.
- [var superlayer: CALayer?](calayer/superlayer.md)
  The superlayer of the layer.
- [func addSublayer(CALayer)](calayer/addsublayer(_:).md)
  Appends the layer to the layer’s list of sublayers.
- [func removeFromSuperlayer()](calayer/removefromsuperlayer.md)
  Detaches the layer from its parent layer.
- [func insertSublayer(CALayer, at: UInt32)](calayer/insertsublayer(_:at:).md)
  Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [func insertSublayer(CALayer, below: CALayer?)](calayer/insertsublayer(_:below:).md)
  Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [func insertSublayer(CALayer, above: CALayer?)](calayer/insertsublayer(_:above:).md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [func replaceSublayer(CALayer, with: CALayer)](calayer/replacesublayer(_:with:).md)
  Replaces the specified sublayer with a different layer object.
### Updating Layer Display
- [func setNeedsDisplay()](calayer/setneedsdisplay.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](calayer/setneedsdisplay(_:).md)
  Marks the region within the specified rectangle as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](calayer/needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func displayIfNeeded()](calayer/displayifneeded.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](calayer/needsdisplay.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](calayer/needsdisplay(forkey:).md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.
### Layer Animations
- [func add(CAAnimation, forKey: String?)](calayer/add(_:forkey:).md)
  Add the specified animation object to the layer’s render tree.
- [func animation(forKey: String) -> CAAnimation?](calayer/animation(forkey:).md)
  Returns the animation object with the specified identifier.
- [func removeAllAnimations()](calayer/removeallanimations.md)
  Remove all animations attached to the layer.
- [func removeAnimation(forKey: String)](calayer/removeanimation(forkey:).md)
  Remove the animation object with the specified key.
- [func animationKeys() -> [String]?](calayer/animationkeys.md)
  Returns an array of strings that identify the animations currently attached to the layer.
### Managing Layer Resizing and Layout
- [var layoutManager: (any CALayoutManager)?](calayer/layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](calayer/setneedslayout.md)
  Invalidates the layer’s layout and marks it as needing an update.
- [func layoutSublayers()](calayer/layoutsublayers.md)
  Tells the layer to update its layout.
- [func layoutIfNeeded()](calayer/layoutifneeded.md)
  Recalculate the receiver’s layout, if required.
- [func needsLayout() -> Bool](calayer/needslayout.md)
  Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [var autoresizingMask: CAAutoresizingMask](calayer/autoresizingmask.md)
  A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [func resize(withOldSuperlayerSize: CGSize)](calayer/resize(witholdsuperlayersize:).md)
  Informs the receiver that the size of its superlayer changed.
- [func resizeSublayers(withOldSize: CGSize)](calayer/resizesublayers(witholdsize:).md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](calayer/preferredframesize.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.
### Managing Layer Constraints
- [var constraints: [CAConstraint]?](calayer/constraints.md)
  The constraints used to position current layer’s sublayers.
- [func addConstraint(CAConstraint)](calayer/addconstraint(_:).md)
  Adds the specified constraint to the layer.
### Getting the Layer’s Actions
- [func action(forKey: String) -> (any CAAction)?](calayer/action(forkey:).md)
  Returns the action object assigned to the specified key.
- [var actions: [String : any CAAction]?](calayer/actions.md)
  A dictionary containing layer actions.
- [class func defaultAction(forKey: String) -> (any CAAction)?](calayer/defaultaction(forkey:).md)
  Returns the default action for the current class.
### Mapping Between Coordinate and Time Spaces
- [func convert(CGPoint, from: CALayer?) -> CGPoint](calayer/convert(_:from:)-8kl76.md)
  Converts the point from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGPoint, to: CALayer?) -> CGPoint](calayer/convert(_:to:)-7dcke.md)
  Converts the point from the receiver’s coordinate system to the specified layer’s coordinate system.
- [func convert(CGRect, from: CALayer?) -> CGRect](calayer/convert(_:from:)-4kx9l.md)
  Converts the rectangle from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGRect, to: CALayer?) -> CGRect](calayer/convert(_:to:)-tly5.md)
  Converts the rectangle from the receiver’s coordinate system to the specified layer’s coordinate system.
- [func convertTime(CFTimeInterval, from: CALayer?) -> CFTimeInterval](calayer/converttime(_:from:).md)
  Converts the time interval from the specified layer’s time space to the receiver’s time space.
- [func convertTime(CFTimeInterval, to: CALayer?) -> CFTimeInterval](calayer/converttime(_:to:).md)
  Converts the time interval from the receiver’s time space to the specified layer’s time space
### Hit Testing
- [func hitTest(CGPoint) -> CALayer?](calayer/hittest(_:).md)
  Returns the farthest descendant of the receiver in the layer hierarchy (including itself) that contains the specified point.
- [func contains(CGPoint) -> Bool](calayer/contains(_:).md)
  Returns whether the receiver contains a specified point.
### Scrolling
- [var visibleRect: CGRect](calayer/visiblerect.md)
  The visible region of the layer in its own coordinate space.
- [func scroll(CGPoint)](calayer/scroll(_:).md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.
- [func scrollRectToVisible(CGRect)](calayer/scrollrecttovisible(_:).md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.
### Identifying the Layer
- [var name: String?](calayer/name.md)
  The name of the receiver.
### Key-Value Coding Extensions
- [func shouldArchiveValue(forKey: String) -> Bool](calayer/shouldarchivevalue(forkey:).md)
  Returns a Boolean indicating whether the value of the specified key should be archived.
- [class func defaultValue(forKey: String) -> Any?](calayer/defaultvalue(forkey:).md)
  Specifies the default value associated with the specified key.
### Constants
- [struct CAAutoresizingMask](caautoresizingmask.md)
  These constants are used by the [`autoresizingMask`](calayer/autoresizingmask.md) property.
- [Action Identifiers](action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](calayer/action(forkey:).md), [`add(_:forKey:)`](calayer/add(_:forkey:).md), [`defaultAction(forKey:)`](calayer/defaultaction(forkey:).md), [`removeAnimation(forKey:)`](calayer/removeanimation(forkey:).md), Layer Filters, and the [`CAAction`](caaction.md) protocol method [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md).
- [struct CAEdgeAntialiasingMask](caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](calayer/magnificationfilter.md) and [`minificationFilter`](calayer/minificationfilter.md).
- [struct CATransform3D](catransform3d.md)
  The standard transform matrix used throughout Core Animation.
### Instance Properties
- [var cornerCurve: CALayerCornerCurve](calayer/cornercurve.md)
- [var wantsDynamicContentScaling: Bool](calayer/wantsdynamiccontentscaling.md)
- [var wantsExtendedDynamicRangeContent: Bool](calayer/wantsextendeddynamicrangecontent.md)
- [var toneMapMode: CALayer.ToneMapMode](calayer/tonemapmode-swift.property.md)
### Type Methods
- [class func cornerCurveExpansionFactor(CALayerCornerCurve) -> CGFloat](calayer/cornercurveexpansionfactor(_:).md)
### Instance Methods
- [func createRemoteLayerBound(to: mach_port_t) -> (any JRSRemoteLayer & NSObjectProtocol)!](calayer/createremotelayerbound(to:).md)
- [func hostRemoteLayer(UInt32)](calayer/hostremotelayer(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CAEAGLLayer](caeagllayer.md)
- [CAEmitterLayer](caemitterlayer.md)
- [CAGradientLayer](cagradientlayer.md)
- [CAMetalLayer](cametallayer.md)
- [CAOpenGLLayer](caopengllayer.md)
- [CAReplicatorLayer](careplicatorlayer.md)
- [CAScrollLayer](cascrolllayer.md)
- [CAShapeLayer](cashapelayer.md)
- [CATextLayer](catextlayer.md)
- [CATiledLayer](catiledlayer.md)
- [CATransformLayer](catransformlayer.md)
### Conforms To
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol CALayerDelegate](calayerdelegate.md)
  Methods your app can implement to respond to layer-related events.
- [class CAConstraint](caconstraint.md)
  A representation of a single layout constraint between two layers.
- [protocol CALayoutManager](calayoutmanager.md)
  Methods that allow an object to manage the layout of a layer and its sublayers.
- [class CAConstraintLayoutManager](caconstraintlayoutmanager.md)
  An object that provides a constraint-based layout manager.
- [protocol CAAction](caaction.md)
  An interface that allows instances to respond to actions triggered by a Core Animation layer change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer)*