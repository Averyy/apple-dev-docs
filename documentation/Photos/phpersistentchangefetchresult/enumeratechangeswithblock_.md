# enumerateChangesWithBlock:

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Executes the block you specify by using the objects in the fetch result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) enumerateChangesWithBlock:(void (^)(PHPersistentChange *change, BOOL *stop)) block;
```

## Parameters

- `block`: The block to apply to elements in the fetch result.

## See Also

### Performing Operations with Objects in a Fetch Request
- [class PHPersistentChange](../phpersistentchange.md)
  An object that represents a change in the Photos library, and allows for requesting local identifiers that identify the changes for a library object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentchangefetchresult/enumeratechangeswithblock:)*