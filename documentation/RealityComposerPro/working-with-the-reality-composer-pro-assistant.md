# Working with the Reality Composer Pro Assistant

**Framework**: Reality Composer Pro

Connect an AI model to Reality Composer Pro to generate assets and get contextual help building scenes.

#### Overview

The Reality Composer Pro **Assistant** connects an AI model to Reality Composer Pro so you can get feature guidance, generate 3D assets and materials, and manage your scene hierarchy. You can ask the Assistant how to use Reality Composer Pro features, request that it generate assets from prompts or attached images, and direct it to reorganize entities in your scene.

#### Add a Model Provider

In the Inspector, click the **Assistant** tab (top right) to open the Assistant panel. Click the **Settings** (gear) icon at the bottom of the panel to open Assistant Settings, then click **Add a Model Provider**. In the dialog, enter a **URL**, an optional **API Key**, an **API Key Header**, and a **Description**, then click **Create**.

> **Note**: Keep your API key confidential. Do not share it or commit it to source control.

![Screenshot of the assistant's settings option](https://docs-assets.developer.apple.com/published/3603e32c2a494b2d80e5fd94033dc248/AssistSettings%402x.png)

To add more AI models, repeat this process with any compatible AI model provider.

#### Use the Assistant

At the top of the Inspector, click the **Assistant** tab. In **New Conversation**, enter your prompt and press Return. The Assistant responds in the conversation panel. To start a fresh conversation, click **New Conversation**. You can also attach image files to your prompt by dragging them into the conversation panel.

#### Explore Prompt Ideas

Experiment with different prompts to discover what the Assistant can do.

> 💡 **Tip**: You can open multiple Assistant tabs, each working on a different prompt. From the Reality Composer Pro main menu, click **Tab** > **New Tab** > **Assistant**.

**Ask about features**

Ask the Assistant how to use specific Reality Composer Pro features.

- “What is the Shader Graph and how do I use it?”
- “What is a Script Graph used for?”
- “How do I create a prototype?”

**Generate assets from a prompt**

Ask the Assistant to generate assets. Add as much or as little detail as needed in your prompt.

> **Note**: The Assistant automatically places generated assets in the Generated Assets and Generated Materials folders.

- “Make a living room scene.”
- Attach an image of a real-world object or space and ask the Assistant to create a scene or model from it. For example, “Make a living room area based on the attached image.”

> **Note**: Avoid attaching images that contain personal information. Content you attach, along with your prompts and conversation history, is sent to the model provider you have configured. Review your model provider’s privacy policy to understand how they handle your data.

**Generate an image, then create a model from it**

You can also ask the Assistant to generate a new image itself, then use that AI-generated image to build a 3D model — no user-supplied photo required.

- “Create an image of a moose.”
- “Create an image of a moose, and then create a model based on the image.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-reality-composer-pro-assistant)*