# unarchivedObject(ofClasses:from:device:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class func unarchivedObject(ofClasses classes: Set<AnyHashable>, from data: Data, device: any MTLDevice) throws -> Any
```

```objc
+ (id) unarchivedObjectOfClasses:(NSSet<Class> *) classes fromData:(NSData *) data device:(id<MTLDevice>) device error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskeyedunarchiver/unarchivedobject(ofclasses:from:device:))*