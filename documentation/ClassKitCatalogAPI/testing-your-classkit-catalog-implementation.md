# Testing Your ClassKit Catalog Implementation

**Framework**: ClassKit Catalog API

Verify your server interaction before deployment by operating in a development environment.

#### Overview

Before you deploy your ClassKit Catalog API changes, you can test them in a development environment that isn’t available to teachers. Use a query parameter in your API calls to choose the development environment, and then use a device in development mode to inspect your updates.

> ❗ **Important**:  Contexts that you publish in the development environment may be visible to other developers using the development environment in Schoolwork.

 Contexts that you publish in the development environment may be visible to other developers using the development environment in Schoolwork.

##### Target the Development Environment

For calls that you make to the ClassKit Catalog API, you set the `environment` query parameter. During normal operation, you set the value of this parameter to `production`. For example, the following `curl` command retrieves the main app context of an example app:

```shell
% curl -v -X GET "https://classkit-catalog.apple.com/v1/contexts?identifierPath=%5B%22com.apple.example.app%22%5D&locale=en-us&environment=production" -H "Authorization: Bearer <JWT>"
```

When you want to work with the development environment, set the parameter to `development` instead:

```shell
% curl -v -X GET "https://classkit-catalog.apple.com/v1/contexts?identifierPath=%5B%22com.apple.example.app%22%5D&locale=en-us&environment=development" -H "Authorization: Bearer <JWT>"
```

You can read and write the development environment just like the production environment. Data isn’t shared between the two environments.

##### Test Your Changes

After uploading content to the development environment, you can inspect the changes. On an iOS device that you use for development, with the Schoolwork app installed, go to Settings > Developer, and choose ClassKit API.

![Screenshot of the Developer settings on an iPad with ClassKit API shown at the top.](https://docs-assets.developer.apple.com/published/6b5720ec71157b78655e1e00ce1af7ee/media-3671033%402x.png)

Then use the ClassKit Catalog Environment section to choose either the Production or Development environment.

![Screenshot of the ClassKit API developer settings on an iPad.](https://docs-assets.developer.apple.com/published/0090a16cfca0e9ec6e6ca8355fd80530/media-3671032%402x.png)

When you choose Development, the Schoolwork app on that device shows you data you uploaded to the development environment instead of the production environment data.

## See Also

- [Authenticating Calls to the ClassKit Catalog API](authenticating-calls-to-the-classkit-catalog-api.md)
  Establish your identity to the ClassKit Catalog server by providing a cryptographically signed token for each call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/testing-your-classkit-catalog-implementation)*