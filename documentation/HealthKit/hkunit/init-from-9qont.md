# init(from:)

**Framework**: HealthKit  
**Kind**: init

Returns the unit instance described by the provided string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(from string: String)
```

#### Return Value

The unit object described by the string. If the string does not represent a valid unit, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception)).

#### Discussion

You can create unit objects using a string representation of that unit, which is a convenient way to create complex, compound units. A few sample units are shown below.

Unit strings use one or more characters to represent the International System of Units (SI). The unit strings for SI units are listed in the following table.

| String | Unit name | Unit type |
| --- | --- | --- |
| `g` | Grams | Mass |
| `m` | Meters | Length |
| `L` or `l` | Liters | Volume |
| `Pa` | Pascals | Pressure |
| `s` | Seconds | Time |
| `J` | Joules | Energy |
| `K` | Kelvin | Temperature |
| `S` | Siemens | Electrical conductance |
| `mol<molar mass>` | Moles | Mass |

For molar mass, you must include the molar mass (in g/mol) of the item to be weighed. For example, for blood glucose samples, use `mol<180.15588000005408>`.

Each SI unit can also take an optional prefix. Valid prefix strings are listed in the following table.

| Prefix | Name | Multiplier |
| --- | --- | --- |
| `p` | Pico- | 1.0e-12 |
| `n` | Nano- | 1.0e-9 |
| `mc` | Micro- | 1.0e-6 |
| `m` | Milli- | 0.001 |
| `c` | Centi- | 0.01 |
| `d` | Deci- | 0.1 |
| `da` | Deca- | 10 |
| `h` | Hecto- | 100 |
| `k` | Kilo- | 1000 |
| `M` | Mega- | 1.0e6 |
| `G` | Giga- | 1.0e9 |
| `T` | Tera- | 1.0e12 |

The [`HKUnit`](hkunit.md) class also supports a number of non-SI units, as shown in the following table.

| String | Unit name | Unit type |
| --- | --- | --- |
| `oz` | Ounces | Mass |
| `lb` | Pounds | Mass |
| `st` | Stones | Mass |
| `in` | Inches | Length |
| `ft` | Feet | Length |
| `yd` | Yard | Length |
| `mi` | Miles | Length |
| `mmHg` | Millimeters of mercury | Pressure |
| `inHg` | Inches of mercury | Pressure |
| `cmAq` | Centimeters of water | Pressure |
| `atm` | Atmospheres | Pressure |
| `fl_oz_us` | U.S. fluid ounces | Volume |
| `fl_oz_imp` | Imperial fluid ounces | Volume |
| `cup_us` | U.S. cup | Volume |
| `cup_imp` | Imperial cup | Volume |
| `pt_us` | U.S. pint | Volume |
| `pt_imp` | Imperial pint | Volume |
| `min` | Minutes | Time |
| `hr` | Hours | Time |
| `d` | Days | Time |
| `Hz` | Hertz | Frequency |
| `cal` | Small calories | Energy |
| `Cal` | Large calories | Energy |
| `kcal` | Kilocalories | Energy |
| `degC` | Degrees Celsius | Temperature |
| `degF` | Degrees Fahrenheit | Temperature |
| `dBASPL` | Decibel: Sound Pressure Level | Sound pressure |
| `dBHL` | Decibel: Hearing Level | Sound pressure |
| `IU` | International Unit | Dosage |
| `count` | Count | Count |
| `%` | Percent | Percent |

Of these, the count and percent units deserve special attention. Count units represent raw scalar values. They can be used to represent the number of times an event occurs—for example, the number of steps the user has taken or the number of times the user has used their inhaler. They can also be used as part of a compound unit—for example, the beats portion of beats per minute.

> **Note**:  In HealthKit quantities, count values are stored using `double` data types, even though they are often interpreted as integers.

 In HealthKit quantities, count values are stored using `double` data types, even though they are often interpreted as integers.

The percent unit measures a value between 0.0 and 1.0. HealthKit uses percent units when measuring body fat percentage, oxygen saturation, blood alcohol content, and similar values.

You can create more complex, compound units by mathematically combining multiple individual units. Unit strings can include symbols that indicate multiplication (. or *) or division (/), or raise a unit to a power (^). In compound unit strings, multiplication is evaluated before anything else. Additionally, there can only be one division symbol in the string. Common compound units are shown in the following table.

| String | Unit name | Unit type | Sample type |
| --- | --- | --- | --- |
| `count/min` | Beats per minute | Count/time | Heart rate |
| `mg/dl` | Milligrams per deciliter | Mass/volume | Blood glucose level |
| `ml/kg/min` | Milliliters per kilogram per minute | Volume/mass/time | VO2 Max |
| `L/min` | Liters per minute | Volume/time | Peak Expiratory Flow Rate |

## Parameters

- `string`: A string representation of the unit, such as  ,  , or  .

## See Also

- [var unitString: String](hkunit/unitstring.md)
  A string representation of the unit object.
- [func isNull() -> Bool](hkunit/isnull.md)
  Returns a Boolean value indicating whether the unit is null.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/init(from:)-9qont)*