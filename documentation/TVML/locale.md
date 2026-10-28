# locale

**Framework**: TVML  
**Role**: Article

Sets the locale for the date element.

## Overview

Here’s an example that sets the locale to Thai, which uses the Buddhist calendar. The date displayed is January 19, 2031 based on the [format](./format.md) attribute.

```xml
<date format="MMMM dd, yyyy" locale="th_TH">2574-01-19</date>
```

### Values for locale

- **`<language>_<country>`**: The locale format the date is in.

### Elements that Use locale

- [date](./date.md)

## See Also

### Date Settings
- [format](./format.md)
  Specifies how a date is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/locale)*