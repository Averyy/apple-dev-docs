# completionBlock()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Returns the completion block object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func completionBlock() -> (() -> Void)?
```

```objc
+ (void (^)(void)) completionBlock;
```

#### Discussion

See [`setCompletionBlock(_:)`](./setcompletionblock%28_%29.md) for a description of the role of the completion block object.

## See Also

### Getting and Setting Completion Block Objects
- [class func setCompletionBlock((() -> Void)?)](./setcompletionblock%28_%29.md)
  Sets the completion block object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/completionblock())*