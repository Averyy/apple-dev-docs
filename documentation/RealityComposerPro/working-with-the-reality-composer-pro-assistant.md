# Working with the Reality Composer Pro assistant

**Framework**: Reality Composer Pro

Connect an AI model to Reality Composer Pro to generate assets, organize scenes, and get feature guidance.

#### Overview

The Reality Composer Pro **Assistant** allows you to connect an AI model to Reality Composer Pro and then use it to help you do things such as:

- **Get help** — Ask the Assistant how to use a feature in Reality Composer Pro.
- **Generate assets** — Ask the Assistant to generate assets and models, either based purely on your prompt or from attached image files.
- **Help manage your project** — Ask the Assistant to move and organize entities in your scene hierarchy or perform other bulk operations to help manage your project.

##### Add a Model Provider

1. In the Inspector, click the Assistant tab (top right-hand tab) to open the Assistant panel.
2. In the Assistant panel, click the Settings (Gear) icon at the bottom of the panel to open the Assistant Settings.
3. Click **Add a Model Provider.**
4. In the **Add a Model Provider** dialog, enter the following information: - URL
- API Key
- API Key Header
- Description (optional)
5. Click **Create**.

![Screenshot of the assistant's settings option](https://docs-assets.developer.apple.com/published/3603e32c2a494b2d80e5fd94033dc248/AssistSettings%402x.png)

To add more AI models, repeat this process — for example, Anthropic or OpenAI.

##### Use the Assistant

At the top of the Inspector, click the Assistant tab. In New Conversation, enter your prompt and press Enter.

##### Explore Prompt Ideas

Experiment with different prompts to discover what the Assistant can do.

> **Note**: The Assistant automatically places generated assets in the Generated Assets and Generated Materials folders.

Ask the Assistant about some of its features and how to use them.

- “What is the Shader Graph and how do I use it?”
- “What is a Script Graph used for?”
- “How do I create a prototype?”

Ask the Assistant to generate assets. Add as much or as little detail as needed in your prompt.

- “Make a living room scene.”
- Attach an image of something and ask the Assistant to create a scene or model from it. For example, “Make a living room area based on the attached image”.

Ask the Assistant to create an image, or generate a model from an image.

- “Create an image of a moose.”
- “Create an image of a moose, and then create a model based on the image.”

> 💡 **Tip**: You can have multiple Assistant tabs open at once, each working on a different prompt. From the Reality Composer Pro main menu, click **Tab** > **New Tab** > **AI Assistant.**


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-reality-composer-pro-assistant)*