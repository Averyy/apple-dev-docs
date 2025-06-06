# init(layer:)

**Framework**: Core Animation  
**Kind**: init

Override to copy or initialize custom fields of the specified layer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(layer: Any)
```

#### Return Value

A layer instance with any custom instance variables copied from `layer`.

#### Discussion

This initializer is used to create shadow copies of layers, for example, for the [`presentation()`](calayer/presentation().md) method. Using this method in any other situation will produce undefined behavior. For example, do not use this method to initialize a new layer with an existing layer’s content.

If you are implementing a custom layer subclass, you can override this method and use it to copy the values of instance variables into the new object. Subclasses should always invoke the superclass implementation.

This method is the designated initializer for layer objects in the presentation layer.

## Parameters

- `layer`: The layer from which custom fields should be copied.

## See Also

- [init()](calayer/init.md)
  Returns an initialized `CALayer` object.
- [init(remoteClientId: UInt32)](calayer/init(remoteclientid:).md)
  Initializes a layer with a remote client ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/init(layer:))*