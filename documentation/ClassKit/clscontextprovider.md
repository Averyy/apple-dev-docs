# CLSContextProvider

**Framework**: ClassKit  
**Kind**: protocol

An interface used to tell your ClassKit context provider app extension to update contexts.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol CLSContextProvider
```

#### Overview

The primary class of a ClassKit context provider extension adopts the [`CLSContextProvider`](clscontextprovider.md) protocol. The protocol’s one required method tells the app extension to create or update the descendants of a given context. Schoolwork triggers this method to fill in your context hierarchy incrementally as the teacher browses your app’s content.

You still build contexts in your main app to support your app’s normal operation, as described in [`Advertising your app’s assignable content`](advertising-your-app-s-assignable-content.md). By also creating a context provider app extension, you enable Schoolwork to advertise your content without having to rely on the teacher first running your app.

##### Create a Classkit Context Provider App Extension

Create a ClassKit context provider by adding a new target to your project in Xcode using File > New > Target. Choose the ClassKit context provider template and give it a name.

![Screenshot of ClassKit context provider template selection in Xcode.](https://docs-assets.developer.apple.com/published/82bea54c4066cfdbe2fef00e0c6769fc/media-3125786%402x.png)

Xcode adds several supporting files to your project, including a new source file defining the extension’s primary class that adopts the [`CLSContextProvider`](clscontextprovider.md) protocol. Fill in the empty [`updateDescendants(of:completion:)`](clscontextprovider/updatedescendants(of:completion:).md) method with your implementation.

You typically call on the context-building code of your main app in the app extension to avoid duplicating code. Do this by either linking the app extension against the relevant source files in your main app, or by putting the common code into a framework. For an example of the former, see the sample code in [`Incorporating ClassKit into an Educational App`](incorporating-classkit-into-an-educational-app.md).

For a general discussion about app extensions, see [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Updating contexts
- [func updateDescendants(of: CLSContext, completion: ((any Error)?) -> Void)](clscontextprovider/updatedescendants(of:completion:).md)
  Updates the descendants of the given context.

## See Also

- [Advertising your app’s assignable content](advertising-your-app-s-assignable-content.md)
  Assemble a hierarchy of contexts and declare your app’s assignable content.
- [class CLSContext](clscontext.md)
  An area of your app that represents an assignable task, like a quiz or a chapter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontextprovider)*