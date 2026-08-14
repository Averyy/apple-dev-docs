# Apple Pencil

**Framework**: Apple Pencil

Enhance your iPad app’s user experience by supporting drawing, handwriting, and other features of Apple Pencil.

#### Overview

Apple Pencil is an input accessory for iPad that people rely on for tasks like drawing, sketching, painting, jotting notes, marking up documents, and more. In addition to drawing and handwriting, Apple Pencil can also serve as a pointer and UI interaction tool.

![An illustration that shows a hand holding Apple Pencil and making a mark on a digital drawing canvas.](/images/com.apple.ApplePencil/apple-pencil-framework-hero@2x.png)

As you optimize your app for iPad, there are many ways you can enhance it with Apple Pencil features. Choose the features that make the most sense in the context of your app, and adopt those features using APIs from PencilKit, SwiftUI, and UIKit.

- ****Drawing****: Apple Pencil integrates seamlessly with PencilKit, a framework that lets you incorporate hand-drawn content into your app. PencilKit provides tools for creating, erasing, and selecting pencil strokes on a drawing canvas. You can also implement drawing with high-precision touches from UIKit. Input from Apple Pencil provides data like azimuth, altitude, roll angle, and the amount of force recorded at its tip, which you can use to create rich drawing experiences.
- ****Handwriting****: With Apple Pencil, people can enter handwritten text in any text field, and Scribble automatically converts their handwriting into typed text input. Scribble is available in multiple languages and is on by default. You can also customize Scribble behavior to meet your app’s needs using the Scribble API in UIKit.
- ****Double tap and squeeze****: People can double-tap and squeeze certain models of Apple Pencil to perform actions quickly. People choose which action they want to perform in response to a double tap or squeeze in Settings, or you can implement a custom action that’s specific to your app. You handle a double tap or squeeze using SwiftUI or UIKit.
- ****Haptics****: Apple Pencil Pro can provide tactile feedback by playing haptics. Used sparingly and consistently, haptic feedback can enhance the experience of using Apple Pencil Pro to perform tasks like snapping objects to a grid. You provide haptic feedback using the sensory feedback API in SwiftUI or the feedback generators API in UIKit.
- ****Hover****: When a person holds a supported model of Apple Pencil close above the screen without touching it, the pencil can provide information about the distance of the tip from the screen. You can use this hover distance to create more expressive drawing and input experiences with Apple Pencil. You get this information using hover gestures in UIKit.
- ****Pointers****: Apple Pencil can behave similar to a pointer, like a trackpad or mouse. For example, you can configure your views to provide visual feedback when a person holds Apple Pencil over the view. Add visual feedback to your views during hover using hover events in SwiftUI or pointer interactions in UIKit.

For more details on Apple Pencil features and compatibility, see [`Apple Pencil`](https://developer.apple.comhttps://www.apple.com/apple-pencil/).

###### Related Videos

## Topics

### Essentials
- [Apple Pencil updates](../updates/applepencil.md)
  Learn about important changes to Apple Pencil.
### Drawing
- [Drawing with PencilKit](../pencilkit/drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](../pencilkit/inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [Getting high-fidelity input with coalesced touches](../uikit/getting-high-fidelity-input-with-coalesced-touches.md)
  Learn how to support high-precision touches in your app.
- [Implementing coalesced touch support in an app](../uikit/implementing-coalesced-touch-support-in-an-app.md)
  Learn how to create a simple app that handles coalesced touches.
### Handwriting
- [Customizing Scribble with Interactions](../pencilkit/customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Handwriting recognition](../uikit/handwriting-recognition.md)
  Configure text fields and custom views that accept text to handle input from Apple Pencil.
### Double tap and squeeze
- [Apple Pencil interactions](../uikit/apple-pencil-interactions.md)
  Handle user interactions like double tap and squeeze on Apple Pencil.
- [Handling squeezes from Apple Pencil](handling-squeezes-from-apple-pencil.md)
  Detect and respond to squeezes a person makes on Apple Pencil Pro.
- [Handling double taps from Apple Pencil](handling-double-taps-from-apple-pencil.md)
  Detect and respond to double taps a person makes on Apple Pencil.
### Haptics
- [Playing haptic feedback in your app](playing-haptic-feedback-in-your-app.md)
  Provide tactile feedback when people perform certain actions in your app.
### Hover
- [Adopting hover support for Apple Pencil](../uikit/adopting-hover-support-for-apple-pencil.md)
  Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
### Pointers
- [Input events](../swiftui/input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Pointer interactions](../uikit/pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
- [Integrating pointer interactions into your iPad app](../uikit/integrating-pointer-interactions-into-your-ipad-app.md)
  Support touch interactions in your iPad app by adding pointer interactions to your views.
### Design
- [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble)
  Apple Pencil helps make drawing, handwriting, and marking effortless and natural, in addition to performing well as a pointer and UI interaction tool.
- [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)
  Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePencil)*