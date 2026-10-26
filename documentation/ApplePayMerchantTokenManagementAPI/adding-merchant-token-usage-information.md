# Adding merchant token usage information

**Framework**: ApplePayMerchantTokenManagementAPI  
**Role**: Article

Create directories and add files, images, and localization for your merchant token usage information package.

#### Overview

To deliver your merchant token usage information to Apple Pay, create a self-contained package that includes information the system needs to display to your customer, such as:

- A `usageInformation.json` file that contains semantic data about your store, including past and upcoming payments
- Your logo, and images of the goods and services you offer
- Optional localization information

The total size of the source must not exceed 5 MB. To deliver the package, compress the source into a zip file.

##### Create the directory and add files

Create a directory to hold the source file for you merchant token information source file, and add the `usageInformation.json` file that contains the usage information for the merchant token. For more information about the contents of this file, see [`GetMerchantTokenUsageInformationPackageResponse`](../MerchantTokenNotificationServices/getmerchanttokenusageinformationpackageresponse.md).

##### Add directories for localization

To localize the strings and images of your usage information for different languages and regions, add a directory at the top level for each localization. In the name of each directory, identify the language of the localization, and optionally, specify a region. Use the following format:

```
`[language identifier]-[region identifier].lproj`
```

For example, the name for the French localization directory is `fr.lproj`, and the name for the Simplified Chinese directory is `xh-Hans.lproj`. For more information on localization regions and scripts, see [Choosing localization regions and scripts](../Xcode/choosing-localization-regions-and-scripts.md).

Localize an image by adding the location-specific image files to each localization directory. For example, to add localized versions of your merchant logo, add the English version of `merchantLogo@2x.png` and `merchantLogo@3x.png` files to your `en.1proj` folder. Reference your images in the `usageInformation.json` by the filename `merchantLogo`. Provide the same number of resolutions for each localization.

> **Note**:  Adding an image of the same name to the top-level source folder overrides any localized versions.

##### Localize the strings

The system localizes the strings in your usage information using a `strings` file that contains a list of keys and associated localized strings.

Add localized strings to your usage information with the following steps:

1. Set the value of a displayed string in `usageInformation.json` to a key.
2. Add a `usageInformation.strings` file to the localization folder.
3. Add a line to each `usageInformation.strings` file that sets a key you create in `usageInformation.json` to the localized term.

The system localizes fields that contain dates and times that use standard formats in the `usageInformation.json` file. The system always displays localized versions of these values, even when your usage information doesn’t contain localization folders for the language. However, the system doesn’t perform currency conversions on fields that contain monetary values; monetary values display in the provided currency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information)*