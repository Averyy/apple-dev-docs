# lockWithPath:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by a given path.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```objc
+ (NSDistributedLock *) lockWithPath:(NSString *) path;
```

## Return Value

An `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by `path`.

## Discussion

For applications to use the lock, `path` must be accessible to—and writable by—all hosts on which the applications might be running.

## Parameters

- `path`: All of `path` up to the last component itself must exist. You can use [`FileManager`](../filemanager.md) to create (and set permissions) for any nonexistent intermediate directories.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
### Creating an NSDistributedLock
- [init?(path: String)](./init%28path%29.md)
  Initializes an `NSDistributedLock` object to use as the lock the file-system entry specified by a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/lockwithpath:)*