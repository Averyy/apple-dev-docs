# DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM

**Framework**: Dispatch  
**Kind**: case  
**Role**: Enumeration Case

The queue configures an autorelease pool before the execution of a block and releases the objects in that pool after the block finishes executing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM
```

## See Also

### Autorelease Frequency Options
- [DISPATCH_AUTORELEASE_FREQUENCY_INHERIT](./dispatch_autorelease_frequency_inherit.md)
  The queue inherits its autorelease frequency from its target queue.
- [DISPATCH_AUTORELEASE_FREQUENCY_NEVER](./dispatch_autorelease_frequency_never.md)
  The queue does not set up an autorelease pool around executed blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_work_item)*