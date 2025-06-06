# initialize()

**Framework**: Objective-C Runtime  
**Kind**: method

Initializes the class before it receives its first message.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func initialize()
```

#### Discussion

The runtime sends [`initialize()`](nsobject-swift.class/initialize().md) to each class in a program just before the class, or any class that inherits from it, is sent its first message from within the program. Superclasses receive this message before their subclasses.

The runtime sends the [`initialize()`](nsobject-swift.class/initialize().md) message to classes in a thread-safe manner. That is, [`initialize()`](nsobject-swift.class/initialize().md) is run by the first thread to send a message to a class, and any other thread that tries to send a message to that class will block until [`initialize()`](nsobject-swift.class/initialize().md) completes.

The superclass implementation may be called multiple times if subclasses do not implement [`initialize()`](nsobject-swift.class/initialize().md)—the runtime will call the inherited implementation—or if subclasses explicitly call `[super initialize]`. If you want to protect yourself from being run multiple times, you can structure your implementation along these lines:

```objc
+ (void)initialize {
  if (self == [ClassName self]) {
    // ... do the initialization ...
  }
}
```

Because [`initialize()`](nsobject-swift.class/initialize().md) is called in a blocking manner, it’s important to limit method implementations to the minimum amount of work necessary possible. Specifically, any code that takes locks that might be required by other classes in their [`initialize()`](nsobject-swift.class/initialize().md) methods is liable to lead to deadlocks. Therefore, you should not rely on [`initialize()`](nsobject-swift.class/initialize().md) for complex initialization, and should instead limit it to straightforward, class local initialization.

##### Special Considerations

[`initialize()`](nsobject-swift.class/initialize().md) is invoked only once per class. If you want to perform independent initialization for the class and for categories of the class, you should implement [`load()`](nsobject-swift.class/load().md) methods.

## See Also

- [init()](nsobject-swift.class/init.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [class func load()](nsobject-swift.class/load.md)
  Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/initialize())*