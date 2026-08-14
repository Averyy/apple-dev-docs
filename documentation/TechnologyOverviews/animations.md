# Animations

**Framework**: Technology Overviews

Add motion to your app’s interface to entertain or provide feedback.

Apps use view-based animations to convey what’s going on, so consider the role that animations play in your app’s interface. Many standard views use animations to convey appearance changes. For example, buttons animate changes for hover events or when someone taps or clicks them. You can add custom animations to support other types of interactions with your content.

If you’re creating a game or immersive experience, frequent animations might be an inherent part of your content. If you’re drawing all of your game’s content, animations are implicit. For apps with 3D content, consider using [`RealityKit`](https://developer.apple.com/documentation/realitykit) to animate your content instead of drawing everything yourself.

> **Note**: Before adding animations to your app, consider their overall impact on your app’s interface and experience. For guidance, read [`Motion`](https://developer.apple.com/design/human-interface-guidelines/motion) in Human Interface Guidelines.

#### Animate the Views in Your Interface

View-based animations convey the state of your app, provide feedback and instruction, and enrich people’s experience with your app. When you use standard system views, you get many animations for free. For example, [`Navigation`](https://developer.apple.com/documentation/swiftui/navigation) in SwiftUI, and view controllers in [`View controllers`](https://developer.apple.com/documentation/uikit/view-controllers) and [`View Management`](https://developer.apple.com/documentation/appkit/view-management) use animations to show transitions between different parts of the interface. If you use these types in your interface, don’t modify or change the built-in animations, which have specific and well-defined meanings.

If you’re defining a new way to present content, consider how you can use animations to support transitions. You can make views appear or disappear, change their visibility, scale or rotate them, and more by changing the view’s built-in attributes. To animate those changes, wrap them in system-provided animation APIs. The following examples use the animation APIs for [`Animations`](https://developer.apple.com/documentation/swiftui/animations), [`Animation and haptics`](https://developer.apple.com/documentation/uikit/animation-and-haptics), and [`Animation`](https://developer.apple.com/documentation/appkit/animation) to change the view’s position along the y-axis. The effect causes the view to bounce up and back down, returning to its original position.

**SwiftUI**:

```swift
struct SimpleAnimationView: View {
    var name: String
    @State private var offset = 0.0

    var body: some View {
        Image(systemName: name)
            .offset(y: offset)
            .onTapGesture {
                withAnimation(.bouncy) {
                    offset = -40.0
                } completion: {
                    withAnimation {
                        offset = 0.0
                    }
                }
            }
    }
}
```

**UIKit**:

```swift
class SimpleAnimationView: UIView {
    var name: String = "globe"
    var imageView : UIImageView? = nil
    
    override init(frame: CGRect) {
       super.init(frame: frame)
        configureSubviews()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        configureSubviews()
    }
    
    func configureSubviews() {
        let image = UIImage(systemName: name)
        imageView = UIImageView(image: image)
        self.addSubview(imageView!)
        
        // Fit the image view to the size of the current view.
        imageView!.leadingAnchor.constraint(equalTo: self.leadingAnchor).isActive = true
        imageView!.trailingAnchor.constraint(equalTo: self.trailingAnchor).isActive = true
        imageView!.topAnchor.constraint(equalTo: self.topAnchor).isActive = true
        imageView!.bottomAnchor.constraint(equalTo: self.bottomAnchor).isActive = true
        
        let gesture = UITapGestureRecognizer(target: self, action: #selector(animateImage))
        self.addGestureRecognizer(gesture)
    }
    
    @objc func animateImage() {
        let animator = UIViewPropertyAnimator(duration: 0.3, curve: .easeOut) {
            self.frame.origin.y -= 40
        }
        animator.addCompletion { position in
            let returnAnimation = UIViewPropertyAnimator(duration: 0.3, curve: .easeIn) {
                self.frame.origin.y += 40
            }
            returnAnimation.startAnimation()
        }
        
        animator.startAnimation()
    }
}
```

**AppKit**:

```swift
class SimpleAnimationView: NSView {
    var name: String = "globe"
    var imageView : NSImageView? = nil
    
    override init(frame: CGRect) {
       super.init(frame: frame)
        configureSubviews()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        configureSubviews()
    }
    
    func configureSubviews() {
        let image = NSImage(systemSymbolName: name, accessibilityDescription: nil)
        imageView = NSImageView(image: image!)
        self.addSubview(imageView!)
        
        imageView!.leadingAnchor.constraint(equalTo: self.leadingAnchor).isActive = true
        imageView!.trailingAnchor.constraint(equalTo: self.trailingAnchor).isActive = true
        imageView!.topAnchor.constraint(equalTo: self.topAnchor).isActive = true
        imageView!.bottomAnchor.constraint(equalTo: self.bottomAnchor).isActive = true
        
        let gesture = NSClickGestureRecognizer(target: self, action: #selector(animateImage))
        self.addGestureRecognizer(gesture)
    }
    
    @objc func animateImage() {
        
        NSAnimationContext.runAnimationGroup { context in
            context.duration = 0.3
            context.timingFunction = CAMediaTimingFunction(name: .easeOut)
            
            self.animator().frame.origin.y += 40
        } completionHandler: {
            NSAnimationContext.runAnimationGroup { context in
                context.duration = 0.3
                context.timingFunction = CAMediaTimingFunction(name: .easeIn)
                
                self.animator().frame.origin.y -= 40
            }
        }
    }
}
```

An alternative approach is to animate UIKit and AppKit content with [`Core Animation`](https://developer.apple.com/documentation/quartzcore). [`UIView`](https://developer.apple.com/documentation/uikit/uiview) and [`NSView`](https://developer.apple.com/documentation/appkit/nsview) use Core Animation [`CALayer`](https://developer.apple.com/documentation/quartzcore/calayer) to manage the pixels they display. A layer is a lightweight type that accelerates drawing-related tasks, including animations. You can use layers to manage image-based content that doesn’t require frequent redrawing. Use the Core Animation APIs when you want more precise control over your layer and view-based animations.

#### Animate 2d Content

If your app’s content is entirely custom, and doesn’t rely on standard views, draw everything yourself using [`Metal`](https://developer.apple.com/documentation/metal). You typically use Metal for games, media apps, productivity apps, or content that people create themselves. For example, use it to implement a whiteboard app that supports custom content creation using a variety of different brushes, tools, and creation modes. Only [`Metal`](https://developer.apple.com/documentation/metal) offers the performance you need to animate large amounts of custom content smoothly.

> **Note**: If your app performs sprite-based animations, consider Core Animation and [`Animate the views in your interface`](animations#Animate-the-views-in-your-interface.md) as potential technologies. These technologies work well for moving prerendered content around your interface.

#### Animate 3d Content

If you create 3D content and scenes in advance, you can use [`RealityKit`](https://developer.apple.com/documentation/realitykit) to display and animate that content. RealityKit provides high-performance simulation and rendering capabilities for 3D content. The RealityKit architecture uses an [`Understanding the modular architecture of RealityKit`](https://developer.apple.com/documentation/visionos/understanding-the-realitykit-modular-architecture) (ECS) architecture to manage content and apply animations and other changes efficiently. Instead of modifying your content, modify components that influence the content. For example, change the position, size, and orientation of an object in your scene by modifying its [`Transform`](https://developer.apple.com/documentation/realitykit/transform). RealityKit takes the component values you provide and applies them to your content during rendering.

When you need raw performance, build your own 3D rendering engine using [`Metal`](https://developer.apple.com/documentation/metal). When you use Metal for drawing, you control what you draw and how you draw it, and Metal runs your code with minimal overhead on the GPU. Use Metal to achieve 3D scenes with realistic lighting, textures, and even special effects like smoke, lens flares, motion blurs, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/animations)*