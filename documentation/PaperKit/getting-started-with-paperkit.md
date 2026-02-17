# Integrating PaperKit into your app

**Framework**: PaperKit

Create your first markup experience by setting up a view controller, adding markup editing tools, and implementing data persistence.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

#### Overview

Whether you’re building a document viewer, note-taking app, design tool, or an app that requires content annotation, PaperKit provides the foundation for rich markup experiences.

To add PaperKit to your existing app, start by creating a [`PaperMarkupViewController`](papermarkupviewcontroller.md) that can save [`PaperMarkup`](papermarkup.md) data to disk and load it back later. Then, integrate PaperKit alongside existing PencilKit code, combining the best of both frameworks.

PaperKit works seamlessly with PencilKit, whether you already use PencilKit in your app or plan to add it. The frameworks complement each other: PencilKit provides freeform drawing capabilities, while PaperKit adds structured markup elements. You can use them together or independently based on your app’s needs.

#### Add a Markup View and Data Model

In PaperKit,  refers to structured annotation elements that your app can add to content. These markup elements include shapes, images, text boxes, and much more. The [`PaperMarkup`](papermarkup.md) data model container handles saving and loading both PaperKit markup and PencilKit drawing data, and it handles rendering the markup on screen.

To create your first markup experience, start by setting up a markup view controller to display content, add editing capabilities for creating markup elements, and then implement data persistence so the system saves the work between app sessions.

[`PaperMarkupViewController`](papermarkupviewcontroller.md) serves as the primary controller for creating and displaying markup content. This controller provides the canvas for viewing and interacting with markup elements overlaid on your content. For example, in a PDF viewer app, this controller displays the PDF content while enabling annotation capabilities. In a note-taking app, it provides the surface for combining text, drawings, and structured markup elements.

The [`PaperMarkup`](papermarkup.md) data model works hand-in-hand with the view controller, storing all the markup data and handling serialization for persistence. You create an instance of the controller, configure it with a [`PaperMarkup`](papermarkup.md) data model, and add it to your view hierarchy.

#### Add Markup Editing Tools

Now that you have a markup view controller displaying content, the next step is to allow markup element creation. [`MarkupEditViewController`](markupeditviewcontroller.md) (UIKit / SwiftUI) and [`MarkupToolbarViewController`](markuptoolbarviewcontroller.md) (AppKit) provide this functionality by presenting a tool palette for selecting and configuring markup tools.

[`PaperMarkupViewController`](papermarkupviewcontroller.md) displays and manages the markup content, while [`MarkupEditViewController`](markupeditviewcontroller.md) and [`MarkupToolbarViewController`](markuptoolbarviewcontroller.md) provide the interface for creating and configuring markup elements. For example, when someone clicks or taps an Add (+) button in your document app, you present this controller to offer choices like text boxes, arrows, signatures, or other markup elements.

#### Save and Load Markup

With your markup view controller set up and editing tools available, the final step in creating your markup experience is to implement data persistence. After creating markup content in your app, you need to save the work so it persists between app launches. PaperKit handles this through the [`PaperMarkup`](papermarkup.md) data model, which can serialize all markup elements — including shapes, text boxes, annotations, and even PencilKit drawings — into a single data representation.

The [`PaperMarkup`](papermarkup.md) data model provides methods to serialize markup content to a format that you can save to disk, similar to how you might save a document or user preferences. When returning to your app, you can load this saved data and restore the markup exactly as someone left it.

This example shows how to save and load markup data, automatically saving when the view disappears to ensure you never lose work.

#### Configure Paperkit with Pencilkit

If your app already uses PencilKit for drawing, PaperKit seamlessly integrates to add structured markup capabilities alongside existing freeform drawing features. This combination enables natural sketching with Apple Pencil while also providing precise, editable markup elements.

For example, in an architectural app, you might sketch rough building layouts with freeform drawing in PencilKit, then add precise measurements and labels using structured text boxes and shapes in PaperKit. In a design review app, people could annotate mockups with both freehand sketches and formal callout boxes.

Structured markup elements are predefined, editable objects like rectangles, arrows, text boxes, and signatures that maintain their properties and that people can easily move, resize, or modify. Unlike freeform drawings, these elements remain sharp at any zoom level, and you can programmatically manipulate them.

Configure your markup view controller to work with existing PencilKit drawing capabilities. The integration maintains separate layers for drawing and markup, ensuring optimal performance and editing flexibility while allowing both types of content to coexist seamlessly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/getting-started-with-paperkit)*