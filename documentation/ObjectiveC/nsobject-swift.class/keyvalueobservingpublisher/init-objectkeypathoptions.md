# init(object:keyPath:options:)

**Framework**: Objective-C Runtime  
**Kind**: init

Creates a key-value observing publisher for the given combination of object and key path, using publishing behavior options you provide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
init(object: Subject, keyPath: KeyPath<Subject, Value>, options: NSKeyValueObservingOptions)
```

#### Discussion

This publisher produces a new element every time the observed property changes.

## Parameters

- `object`: The object that contains the property to publish.
- `keyPath`: The key path, relative to the object receiving this message, of the property to publish.
- `options`: Options that determine which elements the publisher produces. Set this parameter to   to receive new elements when the observed property changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init(object:keypath:options:))*