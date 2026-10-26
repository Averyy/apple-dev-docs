# loadPlugIn:allowNonExecutable:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Loads filters from an image unit that have the appropriate executable status.

**Availability**:
- macOS 10.4+ - Deprecated in 10.7

> **Deprecated**: Instead use [`load(_:allowExecutableCode:)`](./load%28_,allowexecutablecode%29.md).

## Declaration

```objc
+ (void) loadPlugIn:(NSURL *) url allowNonExecutable:(BOOL) allowNonExecutable;
```

#### Discussion

You need to call this method only once to load a specific image unit. The behavior of this method is not defined for multiple calls for the same image unit.

## Parameters

- `url`: The location of the image unit to load.
- `allowNonExecutable`: `TRUE` to load only those filters that are marked by the image unit as non-executable filters.

## See Also

### Deprecated
- [class func loadAllPlugIns()](./loadallplugins%28%29.md)
  Scans directories for files that have the `.plugin` extension and then loads the image units.
- [class func load(URL!, allowExecutableCode: Bool)](./load%28_,allowexecutablecode%29.md)
  Loads filters from an image unit that have the appropriate executable status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/loadplugin:allownonexecutable:)*