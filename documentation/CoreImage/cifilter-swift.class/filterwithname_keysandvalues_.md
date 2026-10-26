# filterWithName:keysAndValues:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a [`CIFilter`](../cifilter-swift.class.md) object for a specific kind of filter and initializes the input values with a `nil`-terminated list of arguments.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```objc
+ (CIFilter *) filterWithName:(NSString *) name keysAndValues:(id) key0;
```

#### Return Value

A [`CIFilter`](../cifilter-swift.class.md) object whose input values are initialized.

#### Discussion

As with all Objective-C methods that accept `nil`-terminated argument lists, to prevent unintended behavior you must take take care not to pass a `nil` value before the intended end of the argument list. You can avoid such issues by using the [`init(name:withInputParameters:)`](./init%28name,withinputparameters%29.md) method to create a filter, expressing the parameter list as a dictionary literal.

## Parameters

- `name`: The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.
- `key0`: A list of key-value pairs to set as input values to the filter. Each key is a constant that specifies the name of the input value to set, and must be followed by a value. You signal the end of the list by passing a `nil` value.

## See Also

### Creating a filter
- [init?(name: String)](./init%28name%29.md)
  Creates a [`CIFilter`](../cifilter-swift.class.md) object for a specific kind of filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filterwithname:keysandvalues:)*