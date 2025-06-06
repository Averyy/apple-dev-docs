# init(forFunction:arguments:)

**Framework**: Foundation  
**Kind**: init

Creates an expression that invokes one of the predefined functions.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forFunction name: String, arguments parameters: [Any])
```

#### Return Value

A new expression that invokes the function `name` using the parameters in `parameters`.

#### Discussion

The `name` parameter can be one of the following predefined functions.

| Function | Parameter | Returns | Availability |
| --- | --- | --- | --- |
| `average:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the average of values in the array) | OS X v10.4 and later |
| `sum:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the sum of values in the array) | OS X v10.4 and later |
| `count:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the number of elements in the array) | OS X v10.4 and later |
| `min:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the minimum of the values in the array) | OS X v10.4 and later |
| `max:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the maximum of the values in the array) | OS X v10.4 and later |
| `median:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the median of the values in the array) | OS X v10.5 and later |
| `mode:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSArray` object (the mode of the values in the array) | OS X v10.5 and later |
| `stddev:` | An `NSArray` object containing `NSExpression` objects representing numbers | An `NSNumber` object (the standard deviation of the values in the array) | OS X v10.5 and later |
| `add:to:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the sum of the values in the array) | OS X v10.5 and later |
| `from:subtract:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the result of subtracting the second value in the array from the first value in the array) | OS X v10.5 and later |
| `multiply:by:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the result of multiplying the values in the array) | OS X v10.5 and later |
| `divide:by:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the result of dividing the first value in the array by the second value in the array) | OS X v10.5 and later |
| `modulus:by:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the remainder of dividing the first value in the array by the second value in the array) | OS X v10.5 and later |
| `sqrt:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the square root of the value in the array) | OS X v10.5 and later |
| `log:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the log of the value in the array) | OS X v10.5 and later |
| `ln:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the natural log of the value in the array) | OS X v10.5 and later |
| `raise:toPower:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the result of raising the first value in the array to the power of the second value in the array) | OS X v10.5 and later |
| `exp:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the base-e exponential of the value in the array) | OS X v10.5 and later |
| `ceiling:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the smallest integral value not less than the value in the array) | OS X v10.5 and later |
| `abs:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the absolute value of the value in the array) | OS X v10.5 and later |
| `trunc:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the integral value nearest to but no greater than the value in the array) | OS X v10.5 and later |
| `random` | `nil` | An `NSNumber` object (a random integer value) | OS X v10.5 and later |
| `random:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (a random integer value between `0` and the value in the array (exclusive)) | OS X v10.5 and later |
| `now` | `nil` | An `[NSDate]` object (the current date and time) | OS X v10.5 and later |
| `floor:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object | iOS 3.0 and later |
| `uppercase:` | An `NSArray` object containing one `NSExpression` object representing a string | An `NSString` object | iOS 3.0 and later |
| `lowercase:` | An `NSArray` object containing one `NSExpression` object representing a string | An `NSString` object | iOS 3.0 and later |
| `bitwiseAnd:with:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the number is treated as an `NSInteger`) | iOS 3.0 and later |
| `bitwiseOr:with:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the number is treated as an `NSInteger`) | iOS 3.0 and later |
| `bitwiseXor:with:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the number is treated as an `NSInteger`) | iOS 3.0 and later |
| `leftshift:by:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the number is treated as an `NSInteger`) | iOS 3.0 and later |
| `rightshift:by:` | An `NSArray` object containing two `NSExpression` objects representing numbers | An `NSNumber` object (the number is treated as an `NSInteger`) | iOS 3.0 and later |
| `onesComplement:` | An `NSArray` object containing one `NSExpression` object representing a number | An `NSNumber` object (the number is treated as an `NSInteger`) | iOS 3.0 and later |
| `noindex:` | An `NSArray` object containing an `NSExpression` object | The result of evaluating the parameter as though the `noindex:` function expression didn’t exist. | iOS 3.0 and later |

This method raises an exception immediately if the selector is invalid; it raises an exception at runtime if the parameters are incorrect.

The `parameters` argument is a collection containing an expression which evaluates to a collection, as illustrated in the following examples:

```objc
NSNumber *number1 = [NSNumber numberWithInteger:20];
NSNumber *number2 = [NSNumber numberWithInteger:40];
NSArray *numberArray = [NSArray arrayWithObjects: number1, number2, nil];
 
NSExpression *arrayExpression = [NSExpression expressionForConstantValue: numberArray];
NSArray *argumentArray = [NSArray arrayWithObject: arrayExpression];
 
NSExpression* expression =
    [NSExpression expressionForFunction:@"sum:" arguments:argumentArray];
id result = [expression expressionValueWithObject: nil context: nil];
 
BOOL ok = [result isEqual: [NSNumber numberWithInt: 60]]; // ok == YES
```

```objc
[NSExpression expressionForFunction:@"random" arguments:nil];
 
[NSExpression expressionForFunction:@"max:"
    arguments: [NSArray arrayWithObject:
        [NSExpression expressionForConstantValue:
            [NSArray arrayWithObjects:
                [NSNumber numberWithInt: 5], [NSNumber numberWithInt: 10], nil]]]];
 
[NSExpression expressionForFunction:@"subtract:from:"
    arguments: [NSArray arrayWithObjects:
        [NSExpression expressionForConstantValue: [NSNumber numberWithInt: 5]],
        [NSExpression expressionForConstantValue: [NSNumber numberWithInt: 10]], nil]];
```

##### Special Considerations

This method throws an exception immediately if the selector is unknown; it throws at runtime if the parameters are incorrect.

## Parameters

- `name`: The name of the function to invoke.
- `parameters`: If there is a mismatch between the number of parameters expected and the number you provide during evaluation, an exception may be raised or missing parameters may simply be replaced by   (which occurs depends on how many parameters are provided, and whether you have over- or underflow).

## See Also

- [init(forFunction: NSExpression, selectorName: String, arguments: [Any]?)](nsexpression/init(forfunction:selectorname:arguments:).md)
  Creates an expression that returns the result of invoking a selector with a specified name using specified arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forfunction:arguments:))*