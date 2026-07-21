# Drawing and printing

**Framework**: Technology Overviews

Draw custom content in your app’s views, and print content to a file or available printer.

You can use standard views to display many types of content, and when you need something completely custom you can draw the content yourself. The app-builder frameworks provide the views for your interface, and also provide drawing tools for custom content. Use the types in [`Drawing and graphics`](https://developer.apple.com/documentation/SwiftUI/Drawing-and-graphics), [`Drawing`](https://developer.apple.com/documentation/UIKit/drawing), and [`Drawing`](https://developer.apple.com/documentation/AppKit/drawing) to draw shapes and composite them alongside images and text. As needed, incorporate types and features from [`Core Graphics`](https://developer.apple.com/documentation/CoreGraphics) and other frameworks into your custom drawing code. As your drawing requirements become more complex, or when performance requires it, switch to [`Metal`](https://developer.apple.com/documentation/Metal) to achieve your goals.

Anything you can draw in your app, you can also print. The system offers integrated printing support, including a standard interface to configure print jobs and start the printing process. Print your content to a connected printer or to a PDF file.

#### Draw Custom Content Using a View

When your app’s drawing requirements are moderate, create your content using existing [`Canvas`](https://developer.apple.com/documentation/SwiftUI/Canvas), [`UIView`](https://developer.apple.com/documentation/UIKit/UIView), or [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) views. These views provide the blank canvas and drawing environment you need to add your custom content. In SwiftUI, you use a closure to build your content from [`Shapes`](https://developer.apple.com/documentation/SwiftUI/Shapes) that the framework provides. In UIKit and AppKit, you define your own subclass and add your custom drawing code to it.

With view-based drawing, you use a painter’s model to create the content you want. Each successive drawing command applies a new layer of “paint” to the underlying view or canvas. When a new shape overlaps a previously drawn shape, the new shape obscures or modifies the content underneath. The amount of transparency in each shape determines how the two colors blend together, as do the blend modes and other graphics-related settings you apply. The order in which you draw your shapes also affects the final outcome, with different orders leading to potentially different appearances, as the following illustration shows.

![An illustration that shows two images drawn together in two different ways. The drawing order of the images changes the final output that appears onscreen.](https://docs-assets.developer.apple.com/published/9d6cd101ee1db4e71c401e6cef1356dc/drawing-order.png)

Use types in SwiftUI, UIKit, and AppKit frameworks for most operations, but you can also use types in the Core Graphics framework for some tasks. For exmple, your drawing code might rely on the
[`Core Graphics`](https://developer.apple.com/documentation/CoreGraphics#Geometric-Data-Types) in Core Graphics to specify the placement of content on your drawing canvas. Similarly, some other system frameworks might require you to specify [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) or [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) using Core Graphics types.

In addition to the technologies you use to draw your content, several technologies provide drawing-adjacent capabilities. Incorporate them as needed to support your app’s features.

- [`PencilKit`](https://developer.apple.com/documentation/PencilKit) captures and displays hand-drawn input into a custom view. Add it if you support drawing content using [`Apple Pencil`](https://developer.apple.com/documentation/ApplePencil).
- [`Core Image`](https://developer.apple.com/documentation/CoreImage) performs hardware-accelerated image-based manipulations. Use this framework to apply filters or special effects to your app’s images. For example, use it to blur the content of an image.
- [`PDFKit`](https://developer.apple.com/documentation/PDFKit) displays and manipulates PDF documents and content.
- [`Core Animation`](https://developer.apple.com/documentation/QuartzCore) provides additional drawing infrastructure. The [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) in particular offers ways to accelerate common operations like adding a background color to your view or masking the view’s content.

#### Build a Graphics Engine Using Metal

If drawing is a central feature of your app, [`Metal`](https://developer.apple.com/documentation/Metal) offers the performance to draw that content efficiently. With Metal, you use a set of [`Understanding the Metal 4 core API`](https://developer.apple.com/documentation/Metal/understanding-the-metal-4-core-api) to build your own graphics engine and generate 2D or 3D content frame-by-frame. During the creation of a single frame, Metal runs your custom shader code on the available GPU cores, applying your rendering commands at hardware speeds. Choose Metal when you need to draw complex content at high frame rates, or want to ensure that your drawing code runs as fast as possible.

In addition to drawing, Metal supports [`Compute passes`](https://developer.apple.com/documentation/Metal/compute-passes), [`Ray tracing with acceleration structures`](https://developer.apple.com/documentation/Metal/ray-tracing-with-acceleration-structures), and other features to create your content. Mix these capabilities with your rendering code to update your app’s content and generate more realistic content.

Metal works hand-in-hand with several other frameworks, which supplement its capabilities. [`MetalKit`](https://developer.apple.com/documentation/MetalKit) defines additional types, including a view you can use to integrate Metal content into your existing view hierarchies. [`MetalFX`](https://developer.apple.com/documentation/MetalFX) upscales lower-resolution content in less time than it takes to render that content directly. [`Metal Performance Shaders`](https://developer.apple.com/documentation/MetalPerformanceShaders) provide optimized code to accelerate many common graphics and compute tasks.

If you’re building an immersive app for Apple Vision Pro, combine your Metal graphics engine with the [`Compositor Services`](https://developer.apple.com/documentation/CompositorServices) framework to create a stereoscopic version of your 3D content. Compositor Services provides the information Metal needs to render the same content from two different eye positions, and give your content a three-dimensional appearance.

#### Print Your Apps Content

Printing support is built-in to iOS, iPadOS, macOS, and visionOS, and the system provides extensive support and UI to manage the printing process for you. To add printing support to your app, you perform three tasks:

- Provide UI to initiate the printing process. For example, provide a Print menu item or initiate printing from an [`Activity views`](https://developer.apple.com/design/Human-Interface-Guidelines/activity-views).
- Show the system-provided printing interface from your app.
- Draw your app’s content during the printing operation.

In macOS, add items to your app’s menu bar to print content and configure printer-related information. If your app supports documents, the [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) class manages most of the printing process for you. Alternatively, you can show the system printing interfaces when someone selects your print-related menu items. AppKit provides a [`NSPageLayout`](https://developer.apple.com/documentation/AppKit/NSPageLayout) to configure printing options and a configurable [`NSPrintPanel`](https://developer.apple.com/documentation/AppKit/NSPrintPanel) to start printing. The system manages the behavior of both panels while they’re visible, and delivers a [`NSPrintOperation`](https://developer.apple.com/documentation/AppKit/NSPrintOperation) object to you when it’s time to print. Configure and run that operation to generate a printable version of your app’s content and send it to the printer.

On platforms other than macOS, people typically initiate printing using an [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController), which you configure with a [`print`](https://developer.apple.com/documentation/UIKit/UIActivity/ActivityType-swift.struct/print). To initiate printing directly when someone interacts with your interface, create and configure a [`UIPrintInteractionController`](https://developer.apple.com/documentation/UIKit/UIPrintInteractionController). The controller supports [`AirPrint`](https://developer.apple.comhttps://developer.apple.com/airprint/) and other network-based printing devices.

> **Note**: The system print interfaces support generating PDF files as an alternative to sending your content to a printer. People can use this option to format your content for printing but save it as a file instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/drawing-and-printing)*