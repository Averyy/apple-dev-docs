# NSObject.KeyValueObservingPublisher

**Framework**: Objective-C Runtime  
**Kind**: struct

A Combine publisher that produces a new element whenever the observed value changes.

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
struct KeyValueObservingPublisher<Subject, Value> where Subject : NSObject
```

#### Overview

Use this publisher to integrate a property that’s compliant with key-value observing into a Combine publishing chain. You can create a publisher of this type with the [`NSObject`](nsobject-swift.class.md) instance method `publisher(for:options:)`, passing in the key path and a set of [`NSKeyValueObservingOptions`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservingOptions).

## Topics

### Creating a KVO Publisher
- [init(object: Subject, keyPath: KeyPath<Subject, Value>, options: NSKeyValueObservingOptions)](nsobject-swift.class/keyvalueobservingpublisher/init(object:keypath:options:).md)
  Creates a key-value observing publisher for the given combination of object and key path, using publishing behavior options you provide.
### Inspecting KVO Publisher Properties
- [let object: Subject](nsobject-swift.class/keyvalueobservingpublisher/object.md)
  The object that contains the property to publish.
- [let keyPath: KeyPath<Subject, Value>](nsobject-swift.class/keyvalueobservingpublisher/keypath.md)
  The key path, relative to the object receiving this message, of the property to publish.
- [let options: NSKeyValueObservingOptions](nsobject-swift.class/keyvalueobservingpublisher/options.md)
  Options that determine which elements the publisher produces.
### Instance Methods
- [func didChange() -> Publishers.Map<NSObject.KeyValueObservingPublisher<Subject, Value>, Void>](nsobject-swift.class/keyvalueobservingpublisher/didchange.md)
  Returns a publisher that emits values when a KVO-compliant property changes.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](../Combine/Publisher.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher)*