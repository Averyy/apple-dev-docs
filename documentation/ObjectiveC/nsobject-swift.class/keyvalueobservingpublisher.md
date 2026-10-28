# NSObject.KeyValueObservingPublisher

**Framework**: Objective-C Runtime  
**Kind**: struct  
**Role**: Structure

A Combine publisher that produces a new element whenever the observed value changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
struct KeyValueObservingPublisher<Subject, Value> where Subject : NSObject
```

## Overview

Use this publisher to integrate a property that’s compliant with key-value observing into a Combine publishing chain. You can create a publisher of this type with the [`NSObject`](../nsobject-swift.class.md) instance method `publisher(for:options:)`, passing in the key path and a set of [`NSKeyValueObservingOptions`](../../Foundation/nskeyvalueobservingoptions.md).

## Topics

### Creating a KVO Publisher
- [init(object: Subject, keyPath: KeyPath<Subject, Value>, options: NSKeyValueObservingOptions)](./keyvalueobservingpublisher/init%28object,keypath,options%29.md)
  Creates a key-value observing publisher for the given combination of object and key path, using publishing behavior options you provide.
### Inspecting KVO Publisher Properties
- [let object: Subject](./keyvalueobservingpublisher/object.md)
  The object that contains the property to publish.
- [let keyPath: KeyPath<Subject, Value>](./keyvalueobservingpublisher/keypath.md)
  The key path, relative to the object receiving this message, of the property to publish.
- [let options: NSKeyValueObservingOptions](./keyvalueobservingpublisher/options.md)
  Options that determine which elements the publisher produces.
### Instance Methods
- [func didChange() -> Publishers.Map<NSObject.KeyValueObservingPublisher<Subject, Value>, Void>](./keyvalueobservingpublisher/didchange%28%29.md)
  Returns a publisher that emits values when a KVO-compliant property changes.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Publisher](../../Combine/publisher.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher)*