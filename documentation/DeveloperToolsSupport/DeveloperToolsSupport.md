# DeveloperToolsSupport

**Framework**: DeveloperToolsSupport  
**Kind**: module

Expose custom views and modifiers in the Xcode library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

#### Overview

Using the DeveloperToolsSupport framework, you tell Xcode about your custom SwiftUI views and view modifiers. After adding your views and modifiers, Xcode makes them available to you when you click the Library button (`+`) in Xcode’s toolbar. You can select and drag the custom library items into code, just like you would for system-provided items.

To add items to the library, create a structure that conforms to the [`LibraryContentProvider`](librarycontentprovider.md) protocol and encapsulate any items you want to add as [`LibraryItem`](libraryitem.md) instances. Implement the [`views`](librarycontentprovider/views.md) computed property to add library items containing views. Implement the [`modifiers(base:)`](librarycontentprovider/modifiers(base:).md) method to add items containing view modifiers. Xcode harvests items from all of the library content providers in your project as you work, and makes them available to you in its library.

## Topics

### Library Customization
- [protocol LibraryContentProvider](librarycontentprovider.md)
  A source of Xcode library and code completion content.
- [struct LibraryItem](libraryitem.md)
  A single item to add to the Xcode library.
### Preview Registration
- [protocol PreviewRegistry](previewregistry.md)
  A protocol that the system uses to locate previews at runtime.
- [struct Preview](preview.md)
  A base type that preview macros use to create previews.
- [enum PreviewLayout](previewlayout.md)
  A size constraint for a preview.
- [struct PreviewTrait](previewtrait.md)
  Customizations that you can apply to a preview.
### Resource Definition
- [struct ColorResource](colorresource.md)
  A color resource.
- [struct ImageResource](imageresource.md)
  An image resource.
### Camera Management
- [struct PreviewCamera](previewcamera.md)
  A camera that defines a viewpoint in a preview.
- [struct PreviewCameraBuilder](previewcamerabuilder.md)
  A builder type that composes a collection of cameras for previewing a view in a 3D scene.
### Structures
- [struct PreviewBodyBuilder](previewbodybuilder.md)
  Builder for preview body content within a `#Preview` macro.
- [struct PreviewMacroBodyBuilder](previewmacrobodybuilder.md)
  Builder for preview body content within a `#Preview` macro.
- [struct PreviewUnavailable](previewunavailable.md)
  An error that the system throws when a preview is unavailable at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeveloperToolsSupport)*